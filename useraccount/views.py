from django.shortcuts import render
from djoser.views import UserViewSet
from rest_framework.response import Response
from rest_framework import status, serializers

# from rest_framework.views import APIView
# from django.core.mail import send_mail
# from django.conf import settings
# from django.template.loader import render_to_string 
# from django.core.mail import EmailMessage

class ActivateUser(UserViewSet):
    ''' This view is for creating GET request to verify account activation. '''
    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())

        kwargs['data'] = {'uid': self.kwargs['uid'], "token": self.kwargs["token"]}

        return serializer_class(*args, **kwargs)
    
    def activation(self, request, *args, **kwargs):
        super().activation(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
