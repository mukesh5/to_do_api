from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers.user_serializers import UserSerializer


@api_view(['POST'])
def register_user(request):
    user = UserSerializer(data=request.data)
    if not user.is_valid():
        return Response(status=422, data={'message':'Please send valid data'})
    return Response({'message': 'success'})
