from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from authentication.managers import UserManager

# Create your models here.

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email addres' ,max_length=255, unique=True)
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    second_name = models.CharField(verbose_name='Фамилия', max_length=255)
    photo = models.ImageField(verbose_name='Фото', upload_to='users/photos')
    bio = models.TextField(verbose_name='Биография', max_length=255 )


    is_active = models.BooleanField(verbose_name='', default=False)
    is_staff =models.BooleanField(verbose_name='', default=False)
    is_superuser = models.BooleanField(verbose_name='', default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'second_name', ]
 
objects = UserManager()

def __str__ (self):
    return self.email

class Meta:
    verbose_name = 'Пользователь'
    verbose_name_plular = 'Пользователи'
    