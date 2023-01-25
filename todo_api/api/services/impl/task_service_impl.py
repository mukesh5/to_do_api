from api.repositories.task_repository import TaskRepository
from api.services.core.task_service import TaskService


class TaskServiceImpl(TaskService):
    def __init__(self):
        self.task_repository = TaskRepository()

    def get_all_user_tasks(self, user_id: int) -> []:
        return self.task_repository.get_all_user_tasks(user_id)
