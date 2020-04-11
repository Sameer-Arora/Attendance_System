
# Create your views here.

from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import UserSerializer      # add this
from django.contrib.auth.models import User

class UserView(viewsets.ModelViewSet):       # add this
    serializer_class = UserSerializer          # add this
    queryset = User.objects.all()              # add this