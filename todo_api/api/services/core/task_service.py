from abc import abstractmethod

from api.models.task_models import Task


class TaskService(object):
    @abstractmethod
    def get_all_user_tasks(self, user_id: int) -> []:
        raise NotImplementedError

    @abstractmethod
    def get_task_by_id(self, task_id: int) -> Task:
        raise NotImplementedError
