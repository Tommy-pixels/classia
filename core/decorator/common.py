import time

def singleton(cls, *args, **kwargs):
    """实现单例的装饰器"""
    instance = {}
    def _singleton():
        if(cls not in instance):
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return _singleton

def stopwatch(func):
    """方法执行时间计时器"""
    def _stopwatch(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print('方法 {} 执行时间：{}'.format(func, end_time-start_time))
        return res
    return _stopwatch