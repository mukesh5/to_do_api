from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers.task_serializers import TaskSerializer
from api.supportlib.utils.api_utils import authorize


@api_view(['POST'])
@authorize()
def add_task(request: HttpRequest) -> Response:
    if not request.META.get('is_authorized'):
        return Response(status=401, data={'message': 'Unauthorized'})
    task = TaskSerializer(data={**request.data, **{'user': request.META.get('user')}})
    if not task.is_valid():
        return Response(status=422, data={'message': 'Invalid Data'})
    task.save()
    return Response(data=task.data)
