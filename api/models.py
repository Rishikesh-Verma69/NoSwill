from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,username, email, role, phone_number, password ):
        if not email:
            raise ValueError('User must have an email addrese')
        user = self.model(
            username=username,
            email = self.normalize_email(email),
            role = role,
            phone_number = phone_number
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,username ,email, password=None):
        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            password=password,
            # first_name = first_name,
            # last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    RESTURAUNT = 1
    RECIPIENT = 2
    ROLL_CHOICES = (
        (RESTURAUNT, 'resturaunt'),
        (RECIPIENT, 'recipient'),
    )
    username = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(verbose_name='email', max_length=100, unique=True)
    phone_number = models.CharField(verbose_name='phone number', max_length=12, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLL_CHOICES, blank=True, null=True)
    # password = models.CharField(max_length=100)

    # Required fields
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'role', 'password']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True


class Location(models.Model):
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='users/profile_pictures', blank=True, null=True)
    cover_photo = models.ImageField(upload_to='users/cover_photos', blank=True, null=True)
    address_line_1 = models.CharField(max_length=50, blank=True, null=True)
    address_line_2 = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    pin_code = models.CharField(max_length=6, blank=True, null=True)
    location = models.OneToOneField(Location, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email
    

class invetoryItems(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    item_id = models.CharField(max_length=10, blank=True, null=True)
    item_name = models.CharField(max_length=50, blank=True, null=True)
    item_stock = models.IntegerField(blank=True, null=True)
    item_experey_date = models.DateField(blank=True, null=True)
    item_created_at = models.DateTimeField(auto_now_add=True)
    item_modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name
    
class Donations(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    donation_id = models.CharField(max_length=10, blank=True, null=True)
    donation_name = models.CharField(max_length=50, blank=True, null=True)
    donation_food_name = models.CharField(max_length=50, blank=True, null=True)
    donation_stock = models.IntegerField(blank=True, null=True)
    donation_location = models.OneToOneField(Location, on_delete=models.CASCADE, blank=True, null=True)
    donation_created_at = models.DateTimeField(auto_now_add=True)
    donation_modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.donation_name