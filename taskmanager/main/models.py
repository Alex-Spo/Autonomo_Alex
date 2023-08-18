from django.db import models

class Task(models.Model):
    title = models.CharField('Тема вопроса', max_length=50)
    task = models.TextField('Вопрос')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
