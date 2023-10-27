from django.db import models
from users.models import NULLABLE


class Course(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100)
    preview = models.ImageField(verbose_name='Preview Image Course', upload_to='course_previews/',  **NULLABLE)
    description = models.TextField(verbose_name='Description')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100)
    description = models.TextField(verbose_name='Description')
    preview = models.ImageField(verbose_name='Preview Image Lesson', upload_to='lesson_previews/',  **NULLABLE)
    video_link = models.URLField(verbose_name='Video Link',  **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
