"文本分类任务"
from core.base.task.base import Base_Task
from core.decorator.common import singleton
from core.base.preprocessing.base import BaseUtil_Handle_Text
from preprocessing.pre_text.cleaner import Cleaner_Text

@singleton
class Text_Classification_Task(Base_Task, BaseUtil_Handle_Text):
    """文本分类任务"""
    def process_steps(self, content:str, *args, **kwargs):
        text_cleaner = Cleaner_Text()
        # 1 文本清洗 洗掉所有标签（由<>包括着的内容）,无关标点等符号
        cleaned_content = text_cleaner.start_process(content=content)
        # 2 文本分词
        cuttedword_generator = self.cut_word(content=cleaned_content)
        # 3 去除停用词
        stopwords_path = r'E:\Projects\classia\static\stopwords\baidu_stopwords.txt'  # 停用词文本路径
        res = self.clean_stopwords(cuttedword_generator=cuttedword_generator, stopwords_path=stopwords_path)
        return res
