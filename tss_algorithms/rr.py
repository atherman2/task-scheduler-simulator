from tss_algorithms.algorithm import *
from tss_tasks.task import *
from collections import deque

class RRTask(Task):

    def __init__(self, task: Task, quantum: int):

        self.id = task.id
        self.duration = task.duration
        self.remaining_time = task.remaining_time
        self.priority = task.priority

        self.restart_remaining_processor_time(quantum)

    def restart_remaining_processor_time(self, quantum: int):

        self.remaining_processor_time = min(quantum, self.duration)

class RRAlgorithm(Algorithm):

    def __init__(self, quantum: int):
        
        self._tasks_deque: deque[RRTask] = deque()
        self.quantum = quantum
    
    def get_scheduled_task(self, new_task=TaskEnum.NO_TASK):
        
        if new_task != TaskEnum.NO_TASK:

            self._tasks_deque.append(RRTask(new_task, self.quantum))
        while True:

            if len(self._tasks_deque) == 0:

                return TaskEnum.NO_TASK
            if self._tasks_deque[0].remaining_time <= 0:

                self._tasks_deque.popleft()
            if self._tasks_deque[0].remaining_processor_time <= 0:

                withdrawed_task = self._tasks_deque.popleft()
                withdrawed_task.restart_remaining_processor_time(self.quantum)
                self._tasks_deque.append(withdrawed_task)
            else:

                task = self._tasks_deque[0]
                task.remaining_time -= 1
                task.remaining_processor_time -= 1
                return task
