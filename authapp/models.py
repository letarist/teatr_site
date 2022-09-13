from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    age = models.PositiveSmallIntegerField(verbose_name='Возраст', blank=True, null=True)
    avatar = models.ImageField(verbose_name='Аватар', blank=True, null=True, upload_to='users_avatar')

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
