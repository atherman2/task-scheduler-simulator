from tss_algorithms.algorithm import *
from tss_tasks.task import *

class SRTFAlgorithm(Algorithm):

    def __init__(self):
        
        self.waiting_tasks: list[Task] = []
        self.active_task: Task = TaskEnum.NO_TASK
    
    def get_scheduled_task(self, new_tasks=[]):
        
        for task in new_tasks:

            self.waiting_tasks.append(task)
        if self.active_task != TaskEnum.NO_TASK:

            scheduled_task = self.active_task
            self.active_task.remaining_time -= 1
            if self.active_task.remaining_time <= 0:

                self.active_task = TaskEnum.NO_TASK
        else:

            self.active_task = self._get_shortes_time_remaining_task()
            self.waiting_tasks.remove(self.active_task)
            scheduled_task = self.active_task
            self.active_task.remaining_time -= 1
            if self.active_task.remaining_time <= 0:

                self.active_task = TaskEnum.NO_TASK
        return scheduled_task
    
    def _get_shortes_time_remaining_task(self) -> Task:

        if len(self.waiting_tasks) == 0:

            return TaskEnum.NO_TASK
        else:

            shortest_job_task = self.waiting_tasks[0]
            for i in range(1, len(self.waiting_tasks)):

                task = self.waiting_tasks[i]
                if task.duration < shortest_job_task.duration:

                    shortest_job_task = task
            return shortest_job_task
