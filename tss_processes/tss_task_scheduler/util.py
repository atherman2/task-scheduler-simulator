from tss_tasks.task import *
from math import ceil

def task_history_to_string(task_history: list[Task]):

    string_history = ""
    if len(task_history) > 0:

        string_history = task_history[0].id
    for i in range(1, len(task_history)):

        string_history += f";{task_history[i].id}"
    return string_history

def task_turnaround_time(task_ready_time: int, task_end_time: int):

    return task_end_time - task_ready_time

def task_waiting_time(task: Task, task_turnaround_time: int):

    return task_turnaround_time - task.duration

def round_one_decimal_digit_up(num: int):

    num *= 10
    num = ceil(num)
    num /= 10
    return num
