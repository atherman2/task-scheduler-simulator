from tss_algorithms.algorithm import *
from tss_tasks.task import Task
from collections import deque

class FcfsAlgorithm(Algorithm):

    def __init__(self):
        
        self._tasks_deque: deque[Task] = deque()
    
    def get_scheduled_task(self, new_task=None):
        
        if new_task != None:

            self._tasks_deque.append(new_task)
        while True:

            if len(self._tasks_deque) == 0:

                return "no task"
            if self._tasks_deque[0].remaining_time <= 0:

                self._tasks_deque.popleft()
            else:

                task = self._tasks_deque[0]
                task.remaining_time -= 1
                return task
