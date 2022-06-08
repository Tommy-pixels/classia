# 分类库 
## 1、功能 
### 1 文本处理 【文本清洗， 分词，去除停用词，文本向量化等操作。】
### 2 文本分析
    - 能够通过Python统计词频，生成词云图。【描述性统计分析】
    - 能够通过方差分析，进行特征选择。【验证性统计分析】
    - 能够根据文本内容，对文本数据进行分类。【统计建模】

## 2、自定义任务
### 1 文本（文章）分类 - 金融文本文章
    ps: 本任务尚未完成
    - 文本处理
        【清洗】文本清洗
        【分词】将文本分词 分词是将连续的文本，分割成语意合理的若干词汇序列
        【去除停用词】将分词结果 去除停用词
    - 分类方法
        · 指定类别相关关键词是否在文本处理后的词列表中
        · 【统计词频】 词频数高的词作为类别

## 3、具体使用
### 1 文本分类
    调用任务类 from task.text_classification import Text_Classification_Task
    创建对象 text_class_task_instance = Text_Classification_Task()
    运行 text_class_task_instance.run_task(content=content)