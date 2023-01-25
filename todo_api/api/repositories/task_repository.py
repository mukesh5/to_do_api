from api.models.task_models import Task


class TaskRepository(object):
    def get_all_user_tasks(self, user_id: int):
        try:
            return Task.objects.filter(user=user_id)
        except Exception:
            return []
