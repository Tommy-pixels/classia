
class Base_Task:
    def process_steps(self, *args, **kwargs):
        print('请重写 process_steps() 方法： 流程处理步骤')
        return

    def run_task(self, *args, **kwargs):
        """执行任务"""
        res = self.process_steps(*args, **kwargs)
        return res