from tss_algorithms.algorithm import *
from tss_tasks.task import *

class SchedulingEnum(Enum):

    FINISHED = auto()

class TaskScheduler:

    def __init__(self, algorithm: Algorithm):
        
        self.algorithm: Algorithm = algorithm
        self.clock_value = 0
        self.predicted_end_time = 0
        self.task_history = []
    
    def get_scheduled_task(self, new_task: Task=TaskEnum.NO_TASK):

        if new_task != TaskEnum.NO_TASK:
            
            self.predicted_end_time += new_task.duration
            if self.predicted_end_time >= (self.clock_value + 1):

                scheduled_task = self.algorithm.get_scheduled_task(new_task)
            else:

                return SchedulingEnum.FINISHED
        else:

            if self.predicted_end_time < (self.clock_value + 1):

                return SchedulingEnum.FINISHED
            scheduled_task = self.algorithm.get_scheduled_task()
        self.task_history.append(scheduled_task)
        self.clock_value += 1
        return scheduled_task
