from django.urls import path

from api.views.task_view import add_task
from api.views.user_view import register_user, validate_user_login

urlpatterns = [
    path('register_user', register_user, name="register_user"),
    path('login', validate_user_login, name="validate_login"),
    path('add_task', add_task, name="add_task")
]
