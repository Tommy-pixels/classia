# 分类库 
依赖库： jieba freehand
## 1、功能 
### 1 文本处理 【文本清洗， 分词，去除停用词，文本向量化等操作。】
### 2 文本分析
    - 能够通过Python统计词频，生成词云图。【描述性统计分析】
    - 能够通过方差分析，进行特征选择。【验证性统计分析】
    - 能够根据文本内容，对文本数据进行分类。【统计建模】

## 2、工具
### 1 方法计时器 统计实处方法执行时间
    from core.decorator.common import stopwatch
    @stopwatch
    def func(*args, *kwargs):
        pass
### 2 单例 将指定类设置为单例
    from core.decorator.common import singleton
    @singleton
    class Singleton:
        pass

## 3、自定义任务
### 1 文本（文章）分类 - 金融文本文章
    采用方法：传统方法
        文本预处理 - 提取特征 - 特征输入分类器 - 输出结果
        目前本任务中 特征为分词统计结果，对特征的分类采用 词匹配的方式，自定义选择特征比例进行匹配分类，分类步骤跟传统方法采用的分类器方法有差异，后续再继续改进优化。
    - jieba 分词词性
        '股票': 名词 n
        '港股': 名词 n
        '美股': 其它专名 nz 、量词 m
        '基金': 名词 n
        'ETF': 英文 eng
        '可转债': 习用语 l
        '贷款': 名词 n
        '融资': 名动词 vn
        '理财': 动词 v
        '指标公式': 名词 n
        '主力': 名词 n
        '游资': 名动词 vn
        '行情': 名词 n
    - 文本处理
        【清洗】文本清洗
        【分词】将文本分词 分词是将连续的文本，分割成语意合理的若干词汇序列
        【去除停用词】将分词结果 去除停用词
    - 分类方法
        · 指定类别相关关键词是否在文本处理后的词列表中
        · 【统计词频】 词频数高的词作为类别
    - 注意：
        · 这里的分类判断根据中文和英文作了不同的对比方法，因为英文句子自带空格，消除空格之后会使得分词结果为多个英文组合在一起的新的词，导致判读出错
            如 JNK ETF的分词结果为JNKETF
        · 其它类型分类: 
            可以通过修改静态资源文件的financial_word_dic.py文件 
            或者通过引用其它自定义类型的分类静态资源文件 from static.word_dicts.fincial_word_dic import TITLE_TAG
            另外需要根据新增的不同词的不同词性在任务类里的分词过滤那里做修改，否则可能因为找不到对应分词而分类失败

## 4、具体使用
### 1 文本分类 
    本任务参数说明：
        content:str, stopwords_path=r'E:\Projects\classia\static\stopwords\baidu_stopwords.txt', default_tag:str='行情', classification_ciping_pattern:str='len', default_ciping_ratio:float=0.1, default_ciping_len:int=10
        :param content: 待分类的文本
        :param stopwords_path: 停用词txt文本路径
        :param classification_ciping_pattern: 文本分类 词频截取模式 默认根据长度截取 len 长度截取 ratio 比例截取
        :param default_ciping_ratio: 用于分类的词频列表长度比例 默认0.1 取值 0~1 根据此长度来决定文章分类的精确度 长度越小越精确, 当该值为-1时精确度最低 该值不能取0
        :param default_ciping_len: 类同 default_ciping_ratio， 这里取指定长度词频结果列表进行分类 默认10 , 当该值为-1时精确度最低
        :param default_tag: 若分类结果为空，默认将其归为此类
        :return: res_tag_lis 分类结果
    .run_task(content=content, classification_ciping_pattern='ratio', default_ciping_ratio=0.2)
    .run_task(content=content, classification_ciping_pattern='len', default_ciping_len=15)
    默认情况下 词频截取采用 len模式 取值10：
        调用任务类 from task.text_classification import Text_Classification_Task
        创建对象 text_class_task_instance = Text_Classification_Task()
        运行 text_class_task_instance.run_task(content=content)