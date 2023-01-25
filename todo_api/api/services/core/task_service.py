from abc import abstractmethod


class TaskService(object):
    @abstractmethod
    def get_all_user_tasks(self, user_id: int) -> []:
        raise NotImplementedError
