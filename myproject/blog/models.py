from django.db import models
from django.contrib.auth.models import User  # Убедитесь, что этот импорт присутствует
from django.utils import timezone


class Person(models.Model):
    name = models.CharField('Имя', max_length=200)
    age = models.IntegerField('Возраст', default=0)
    hobbies = models.TextField('Хобби')
    created_at = models.DateTimeField('Дата', default=timezone.now)
    avtor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):  # Исправлено название метода
        return f'Новый пользователь'
