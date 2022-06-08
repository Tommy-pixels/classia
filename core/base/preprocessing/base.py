from freehand.core.base.middleware.mid_string.mid_string_clean import StringMiddleware
import jieba

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
        return [word for word in word_generator if word not in stopword_set]

    @classmethod
    def clean_webtag(cls, content):
        """
        清洗html标签
        :param content: 待清洗的内容
        :return cleaned_content: 清洗完成的结果
        """
        cleaned_content = StringMiddleware.clean_between(content, s_left='<', s_right='>')
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
    def cut_word(cls, content)->list:
        """文本分词
        :param content: 经过清洗的文本
        :return: 分词结果生成器
        """
        return jieba.cut(content)
