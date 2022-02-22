from django.utils import timezone
from django.db import models





class Feedback(models.Model):
    first_name = models.CharField('Имя', max_length=256)
    last_name = models.CharField('Фамилия', max_length=256)
    number = models.CharField('Номер телефона', max_length=256)
    text = models.TextField('Сообщение')
    date = models.DateTimeField('Время', default=timezone.now())


    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

    