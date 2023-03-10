from django.urls import path

from api.views.task_view import add_task, get_all_tasks, update_task, delete_task
from api.views.user_view import register_user, validate_user_login

urlpatterns = [
    path('user/register', register_user, name="register_user"),
    path('user/login', validate_user_login, name="validate_login"),
    path('tasks/add', add_task, name="add_task"),
    path('tasks/all', get_all_tasks, name="get_all_tasks"),
    path('tasks/update/<int:task_id>', update_task, name='update_task'),
    path('tasks/delete/<int:task_id>', delete_task, name='delete_task')
]