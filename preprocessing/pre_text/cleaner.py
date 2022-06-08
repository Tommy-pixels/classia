from core.base.preprocessing.base import Base_Cleaner, BaseUtil_Handle_Text
import re



class Cleaner_Text(Base_Cleaner, BaseUtil_Handle_Text):
    """文本清洗 通过start_process()方法启动清洗"""
    instance = None

    def __new__(cls, *args, **kwargs):
        if(cls.instance):
            return cls.instance
        else:
            cls.instance = object.__new__(cls)
            return cls.instance

    def process_steps(self, content):
        cleaned_content = self.clean_webtag(content=content)
        unrelative_re_obj = re.compile(
            r"[!\"#$%&'’（）()*+,-;；，.。：:【】《》、?？[\\\]`~·——！“”_{|}￥<=>…\s]+"
        )
        cleaned_content = self.clean_unrelative(content=cleaned_content, unrelative_re_obj=unrelative_re_obj)
        return cleaned_content