from tss_algorithms.algorithm import *
from tss_tasks.task import *
from tss_processes.tss_task_scheduler.util import *

class SchedulingEnum(Enum):

    FINISHED = auto()

class TaskScheduler:

    def __init__(self, algorithm: Algorithm):
        
        self.algorithm: Algorithm = algorithm
        self.clock_value = 0
        self.predicted_end_time = 0
        self.task_history: list[Task] = []
        self.tasks: dict[str, Task] = {}
        self.tasks_ready_time: dict[str, int] = {}
        self.tasks_end_time: dict[str, int] = {}
    
    def get_scheduled_task(self, new_task: Task=TaskEnum.NO_TASK):

        if new_task != TaskEnum.NO_TASK:

            self.tasks[new_task.id] = new_task
            self.tasks_ready_time[new_task.id] = self.clock_value  
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
        if scheduled_task.remaining_time <= 0:

            self.tasks_end_time[scheduled_task.id] = self.clock_value
        return scheduled_task
    
    def write_output_file(self, output_path:str):

        with open(output_path, "w") as f:

            tasks_turnaround_time = []
            tasks_waiting_time = []
            f.write(f"{task_history_to_string(self.task_history)}\n")
            for task_id, task in self.tasks.items():

                f.write(f"{task_id}")
                ready_time = self.tasks_ready_time[task_id]
                f.write(f";{ready_time}")
                end_time = self.tasks_end_time[task_id]
                f.write(f";{end_time}")
                turnaround_time = task_turnaround_time(ready_time, end_time)
                f.write(f";{turnaround_time}")
                tasks_turnaround_time.append(turnaround_time)
                waiting_time = task_waiting_time(task, turnaround_time)
                f.write(f";{waiting_time}\n")
                tasks_waiting_time.append(waiting_time)
            
            tasks_count = len(self.tasks.items())
            if tasks_count == 0:

                f.write("No tasks were scheduled\n")
            else:

                turnaround_time_mean = sum(tasks_turnaround_time)/tasks_count
                waiting_time_mean = sum(tasks_waiting_time)/tasks_count
                f.write(f"{round_one_decimal_digit_up(turnaround_time_mean)}")
                f.write(f";{round_one_decimal_digit_up(waiting_time_mean)}\n")
