from tss_tasks.task import *

class TaskEmitter:

    def __init__(self, task_dict):
        
        self.clock_value = 0
        self.task_dict = task_dict
    
    def get_new_ready_task(self):

        if self.clock_value in self.task_dict:

            task = self.task_dict[self.clock_value]
        else:

            task = TaskEnum.NO_TASK
        self.clock_value += 1
        return task
    