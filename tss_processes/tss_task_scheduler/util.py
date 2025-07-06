from tss_tasks.task import *

def task_history_to_string(task_history: list[Task]):

    string_history = ""
    if len(task_history) > 0:

        string_history = task_history[0].id
    for i in range(1, len(task_history)):

        string_history += f";{task_history[i].id}"
    return string_history
