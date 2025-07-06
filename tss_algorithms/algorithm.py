from tss_tasks.task import *

class Algorithm:

    not_implemented_error_message = "Algorithm class works as an interface. Can't call Algorithm's methods"

    def get_scheduled_task(self, new_task=TaskEnum.NO_TASK):

        raise NotImplementedError(Algorithm.not_implemented_error_message)
