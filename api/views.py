from django.shortcuts import render
from rest_framework import generics
from .models import User
# from rest_framework.permissions import 

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = User