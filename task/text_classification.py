"""文本分类任务"""
from core.base.task.base import Base_Task
from core.decorator.common import singleton
from core.base.preprocessing.base import BaseUtil_Handle_Text
from preprocessing.pre_text.cleaner import Cleaner_Text
from static.word_dicts.financial_word_dic import TITLE_TAG
import os

@singleton
class Text_Classification_Task(Base_Task, BaseUtil_Handle_Text):
    """文本分类任务"""
    def process_steps(self, content:str, stopwords_path=os.getcwd()+'\\static\\stopwords\\baidu_stopwords.txt', default_tag:str='行情', classification_ciping_pattern:str='len', default_ciping_ratio:float=0.1, default_ciping_len:int=10, *args, **kwargs)->set:
        """ 文本分类流程
        :param content: 待分类的文本
        :param stopwords_path: 停用词txt文本路径
        :param classification_ciping_pattern: 文本分类 词频截取模式 默认根据长度截取 len 长度截取 ratio 比例截取
        :param default_ciping_ratio: 用于分类的词频列表长度比例 默认0.1 取值 0~1 根据此长度来决定文章分类的精确度 长度越小越精确, 当该值为-1时精确度最低 该值不能取0
        :param default_ciping_len: 类同 default_ciping_ratio， 这里取指定长度词频结果列表进行分类 默认10 , 当该值为-1时精确度最低
        :param default_tag: 若分类结果为空，默认将其归为此类
        :return: res_tag_lis 分类结果
        """
        text_cleaner = Cleaner_Text()
        # 1 文本清洗 洗掉所有标签（由<>包括着的内容）,无关标点等符号
        cleaned_content = text_cleaner.start_process(content=content)
        # 2 文本分词
        cuttedword_generator = self.cut_word(content=cleaned_content, check_wordtag=True)
        # 3 去除停用词
        word_lis = self.clean_stopwords(cuttedword_generator=cuttedword_generator, stopwords_path=stopwords_path)
        # 4 根据词性过滤 根据待分类的词的词性筛选分词列表以避免资源浪费 (美股 被归类到m量词里去了， 美股三大 被归类到nz其它专名里去了 ...)
        filted_word_lis = self.filterby_wordtag(word_lis=word_lis, wordtag_lis=['n', 'eng', 'nz', 'm', 'l', 'vn', 'v'])
        # 5 列表词频统计
        ciping = self.count_word_num(word_lis=filted_word_lis)
        # 6 用于判断的词频列表长度设置
        if(classification_ciping_pattern == 'len'):
            if (int(default_ciping_len) == -1 or (default_ciping_len<1 and default_ciping_len!=0)):
                default_ciping_len = len(ciping)
        elif(classification_ciping_pattern == 'ratio'):
            if (int(default_ciping_ratio) == -1 or default_ciping_ratio<0 or default_ciping_ratio>1):
                default_ciping_len = len(ciping)
            else:
                default_ciping_len = int(len(ciping) * default_ciping_ratio)
        else:
            default_ciping_len = len(ciping)
        ciping = ciping[0: default_ciping_len]
        # 7 遍历字典分类文章
        res_tag_lis = set()
        titletag_keys = list(TITLE_TAG.keys())
        for word, word_num in ciping:
            # 针对英文标签的单独处理 英文句子自带空格 去掉空格后合在一起后影响下面的判断
            for titletag in titletag_keys:
                if(titletag.encode('utf-8').isalpha() and (titletag.upper() in word or titletag.lower() in word)):
                # if(titletag.upper() in word or titletag.lower() in word):
                    res_tag_lis.add(titletag)
                    titletag_keys.pop(titletag_keys.index(titletag))
            # 下面针对中文的分类判断通用处理
            if(word in titletag_keys):
                res_tag_lis.add(word)
                titletag_keys.pop(titletag_keys.index(word))
            else:
                # 遍历相关词
                for tag, tag_lis in TITLE_TAG.items():
                    if(tag in res_tag_lis):
                        continue
                    if(word in tag_lis):
                        res_tag_lis.add(tag)
        if(not res_tag_lis):
            # 若无何时标签通通归类为行情
            res_tag_lis.add(default_tag)
        return res_tag_lis
