from tss_tasks.util import *

def input_file_to_task_dict(path:str) -> dict[int, Task]:

    info_lines = []
    with open(path, "r") as f:

        while (line := f.readline()) != "":

            info_lines.append(line)
    return task_dict(info_lines)
