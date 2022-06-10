import jieba
import jieba.posseg as psg
import re

class Base_Cleaner:
    def process_steps(self, content):
        """清洗步骤 根据不同类型内容重写清洗步骤 根据不同内容重写本方法
        :param content: 待清洗的内容
        :return: cleaned_content 清洗完成的结果
        """
        cleaned_content = content
        return cleaned_content

    def start_process(self, content):
        """启动清洗
        :param content: 待清洗的内容
        :return cleaned_content: 清洗完成的结果"""
        cleaned_content = self.process_steps(content=content)
        return cleaned_content

class BaseUtil_Handle_Text:
    """文本处理类"""
    @classmethod
    def get_stopwords_set(cls, stopwords_path:str)->set:
        """获取停用词set
        :param stopwords_path: 停用词文件路径
        :return: stopword_set
        """
        stopword_set = set()
        with open(stopwords_path, 'r', encoding='UTF-8') as f:
            for line in f:
                stopword_set.add(line.strip())
        return stopword_set

    @classmethod
    def remove_stopword(cls, word_generator:object, stopword_set:set)->list:
        """ 清除停用词
        :param word_lis: 待处理的文本
        :return: 清除停用词后的列表
        """
        return [(word, word_tag) for word, word_tag in word_generator if word not in stopword_set]

    @classmethod
    def clean_between(cls, s, s_left, s_right):
        """去除字符串中指定左右间的内容
            如： s = '财讯网（记者 XXX）AAAAA'     #去除（记者 XXX）
                s = del_content_between(s, s_left='（记者', s_right='）')
        :param s: 待清洗的内容
        :param s_left: 左匹配
        :param s_right: 右匹配
        :return cleaned_content: 清洗完成的结果
        """
        try:
            r_rule = u"\\" + s_left + u".*?" + s_right
            cleaned_s = re.sub(r_rule, "", s)
        except Exception as e:
            r_rule = u"\\" + s_left + u".*?" + "\\" + s_right
            cleaned_s = re.sub(r_rule, "", s)
        return cleaned_s

    @classmethod
    def clean_webtag(cls, content):
        """清洗html标签
        :param content: 待清洗的内容
        :return cleaned_content: 清洗完成的结果
        """
        cleaned_content = cls.clean_between(content, s_left='<', s_right='>')
        return cleaned_content

    @classmethod
    def clean_stopwords(cls, cuttedword_generator, stopwords_path)->list:
        """清除停用词
        :param cuttedword_generator: 经过分词处理的生成器
        :param stopwords_path: 停用词文件路径
        :return: 去除了停用词的列表
        """
        stopword_set = cls.get_stopwords_set(stopwords_path=stopwords_path)
        res = cls.remove_stopword(word_generator=cuttedword_generator, stopword_set=stopword_set)
        return res

    @classmethod
    def clean_unrelative(cls, content:object, unrelative_re_obj:object)->str:
        """清除不想管的标点符号和特殊字符
        :param content: 待处理的经过分词处理的生成器
        :param unrelative_re_obj: 待清洗的re对象
        :return: 清洗过的文本
        """
        return unrelative_re_obj.sub('', content)

    @classmethod
    def cut_word(cls, content, check_wordtag=False)->object:
        """文本分词
        :param content: 经过清洗的文本
        :param check_wordtag: 是否需要获取词性
        :return: 分词结果生成器
        """
        if(check_wordtag):
            return psg.cut(content)
        else:
            return jieba.cut(content)

    @classmethod
    def filterby_wordtag(cls, word_lis:list, wordtag_lis:list=['n', 'eng', 'nz', 'm', 'l'])->list:
        """ 根据词性过滤词列表 默认筛出名词
        词性： 名称 n 英文 eng 其它专名 nz 量词 m 习用语 l 名动词 vn 动词 v
        :param word_lis: 词列表 [(词语, 词性)]
        :param wordtag_lis: 筛选出指定词性的词 列表
        :return: output_lis
        """
        output_lis = []
        for word, tag in word_lis:
            if(tag in wordtag_lis):
                output_lis.append((word, tag))
        return output_lis

    @classmethod
    def count_word_num(cls, word_lis)->list:
        """ 词频统计 输出列表结果 [(词, 数量)]
        :param word_lis: 列表里包含重复的词，通过计数统计词频
        :return: output_lis
        """
        output_lis = []
        duplicated_word_lis = []
        unduplicated_word_lis = set()
        for word, tag in word_lis:
            duplicated_word_lis.append(word)
            unduplicated_word_lis.add(word)
        for w in unduplicated_word_lis:
            word_num = duplicated_word_lis.count(w)
            output_lis.append((w, word_num))
        output_lis = sorted(output_lis, key=lambda x:x[1], reverse=True)
        return output_lis