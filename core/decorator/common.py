
def singleton(cls, *args, **kwargs):
    """实现单例的装饰器"""
    instance = {}
    def _singleton():
        if(cls not in instance):
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return _singleton