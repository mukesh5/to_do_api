from django.core.exceptions import ObjectDoesNotExist

from api.models.task_models import Task


class TaskRepository(object):
    def get_all_user_tasks(self, user_id: int):
        try:
            return Task.objects.filter(user=user_id)
        except Exception:
            return []

    def get_task_by_id(self, task_id: int):
        try:
            user = Task.objects.get(id=task_id)
            return user
        except ObjectDoesNotExist:
            return None

