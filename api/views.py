from django.shortcuts import render
from rest_framework import generics
from .models import User , invetoryItems, UserProfile, Donations
from .serializers import * 
from rest_framework.permissions import  AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

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


class UserLoginView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            # Perform any additional actions like generating tokens, etc.
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
