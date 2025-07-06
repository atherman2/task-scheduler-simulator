from enum import Enum, auto

class TaskEnum(Enum):

    NO_TASK = auto()

class Task:

    def __init__(self, info_list=None):
        
        if info_list != None:

            self.id = info_list[0]
            self.duration = info_list[1]
            self.remaining_time = self.duration
            self.priority = info_list[2]

    def __str__(self):

        return f"[Task: id={self.id}, duration={self.duration}, remaining_time={self.remaining_time} priority={self.priority}]"
