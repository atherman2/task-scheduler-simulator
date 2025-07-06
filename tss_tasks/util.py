from tss_tasks.task import *

def task_dict(info_lines: list[str]) -> dict[int, Task]:

    task_dictionary = {}
    try:
        for info_line in info_lines:
                
            info_line = info_line.split(";")
                
            task_id, task_enter_time, task_duration, task_priority = info_line
            task_enter_time = int(task_enter_time)
            task_duration = int(task_duration)
            task_priority = int(task_priority)

            task_info = [task_id, task_duration, task_priority]
            task_dictionary[task_enter_time] = Task(task_info)
    except Exception:

        raise ValueError("\nERROR: The input must be in the format:\n<task_id:str>;<task_enter_time:int>;<task_duration:int>;<task_priority:int>")
    return task_dictionary
