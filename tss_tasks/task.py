class Task:

    def __init__(self, info_list=None):
        
        if info_list != None:

            self.id = info_list[0]
            self.duration = info_list[1]
            self.priority = info_list[2]

    def __str__(self):

        return f"[Task: id={self.id}, duration={self.duration}, priority={self.priority} ]"
