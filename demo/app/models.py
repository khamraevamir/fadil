from django.utils import timezone
from django.db import models





class Feedback(models.Model):
    first_name = models.CharField('Имя', max_length=256)
    number = models.CharField('Номер телефона', max_length=256)
    text = models.TextField('Сообщение')
    date = models.DateTimeField('Время', default=timezone.now())


    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

    

class Question(models.Model):
    question = models.CharField('Вопрос', max_length=256)
    answer = models.TextField('Ответ')


    class Meta:
        verbose_name = 'Вопросы и ответы'
        verbose_name_plural = 'Вопросы и ответы'


class Gallery(models.Model):
    image = models.ImageField('Фото', upload_to='gallery')


    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Галерея'