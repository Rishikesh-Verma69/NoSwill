from django.shortcuts import render
from rest_framework import generics
from .models import User , invetoryItems, UserProfile, Donations
from .serializers import UserSerializer, CustomTokenObtainPairSerializer , invetoryItemsSerializer , UserProfileSerializer , donationSerializer
from rest_framework.permissions import  AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class inventoryItemsView(generics.ListCreateAPIView):
    queryset = invetoryItems.objects.all()
    serializer_class = invetoryItemsSerializer
    permission_classes = [AllowAny]

class donationView(generics.ListCreateAPIView):
    queryset = Donations.objects.all()
    serializer_class = donationSerializer
    permission_classes = [AllowAny]

class UserProfileView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [AllowAny]