from datetime import datetime
from rest_framework import serializers


from api.models.task_models import Task


class TaskSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(default=datetime.now())
    updated_at = serializers.DateTimeField(default=datetime.now())

    class Meta:
        model = Task
        fields = '__all__'
