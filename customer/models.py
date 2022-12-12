from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
# Create your models here.

class MyCustomerManager(BaseUserManager):
    def create_user(self, name, email,phone, password=None, **extra_fields):
        if not email:
            raise ValueError('Email address is required')

        if not name:
            raise ValueError('User name is required')

        user = self.model(
            email=self.normalize_email(email=email),  
            name=name,
            phone = phone,
            password=password,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, phone, password=None, **extra_fields):
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)


        user = self.create_user(
            name=name,
            email=email,
            phone = phone,
            password=password,
            **extra_fields,
        )
        return user

SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
        ('U', 'Unsure',),
    )
class Customer(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='images_customer', default='images_customer/default.png')
    age = models.IntegerField(default=0)
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        default='U',
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']

    objects = MyCustomerManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return self.email

