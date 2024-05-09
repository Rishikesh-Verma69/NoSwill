from .models import User , invetoryItems , UserProfile, Location ,Donations
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'latitude', 'longitude')

class UserProfileSerializer(serializers.ModelSerializer):
    # location = LocationSerializer(many=True)
    latitude = serializers.CharField(source='location.latitude')
    longitude = serializers.CharField(source='location.longitude')
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'profile_picture', 'address_line_1', 'address_line_2', 'city', 'state', 'country', 'pin_code', 'latitude', 'longitude' , 'created_at' , 'modified_at')



class invetoryItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = invetoryItems
        fields = ('id', 'item_id', 'item_name', 'item_stock', 'item_experey_date', 'item_created_at', 'item_modified_at')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',  'email', 'phone_number' , 'role', 'password')
        extra_kwargs = {"password": {"write_only": True}}


        def create(self, validated_data):
            print(validated_data)
            user = User.objects.create_user(**validated_data)
            return user


class donationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donations
        fields = ('id', 'donation_id', 'donation_name', 'donation_food_name', 'donation_stock', 'donation_location', 'donation_created_at', 'donation_modified_at' )



# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         email = attrs.get("username")
#         password = attrs.get("password")

#         # Ensure both email and password are provided
#         if email and password:
#             userEmail = User.objects.filter(email=email).first()
#             user = authenticate(request=self.context.get('request'), email=userEmail, password=password)

#             if user:
#                 return super().validate(attrs)
#             else:
#                 # If user does not exist, raise validation error
#                 raise serializers.ValidationError("User does not exist.")
#         else:
#             # If email or password is missing, raise validation error
#             raise serializers.ValidationError("Must include email and password.")



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    raise serializers.ValidationError("User account is disabled.")
            else:
                raise serializers.ValidationError("Unable to log in with provided credentials.")
        else:
            raise serializers.ValidationError("Must include 'email' and 'password'.")

        return data
