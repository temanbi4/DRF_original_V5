from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    phone = models.CharField(max_length=30, verbose_name='Номер телефона', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='Город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)

    email = models.EmailField(unique=True, verbose_name='email')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.last_name} {self.first_name} ({self.email})'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'