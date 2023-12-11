from django.conf import settings
from django.db import models
from users.models import NULLABLE


PAYMENT_CURRENCY_CHOICES = [('usd', 'usd'), ('rub', 'rub')]


class Course(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100)
    preview = models.ImageField(verbose_name='Preview Image Course', upload_to='course_previews/',  **NULLABLE)
    description = models.TextField(verbose_name='Description')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='владелец', **NULLABLE)
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Стоимость курса', **NULLABLE)
    currency = models.CharField(max_length=20, choices=PAYMENT_CURRENCY_CHOICES, verbose_name='Валюта', default='rub')
    is_buy = models.BooleanField(default=False)

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
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курсы', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='владелец', **NULLABLE)
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Стоимость урока', **NULLABLE)
    currency = models.CharField(max_length=20, choices=PAYMENT_CURRENCY_CHOICES, verbose_name='Валюта', default='rub')
    is_buy = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Payment(models.Model):

    PAYMENT_CHOICES = [
        ('Cash', 'Наличные'),
        ('Transfer', 'Перевод')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь',
                             **NULLABLE)
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='оплаченный урок', **NULLABLE)
    payment_amount = models.PositiveIntegerField(verbose_name='Сумма оплаты')
    payment_method = models.CharField(max_length=150, choices=PAYMENT_CHOICES, verbose_name='Способ оплаты')
    payment_currency = models.CharField(choices=PAYMENT_CURRENCY_CHOICES,
                                        max_length=255, verbose_name='Валюта',
                                        default='rub')

    def __str__(self):
        return f'{self.course if self.course else self.lesson} ({self.payment_date})'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь',
                             **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    is_active = models.BooleanField(default=True, verbose_name='активна')

    def __str__(self):
        return f'Подписка на курс {self.course} для пользователя {self.user}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'