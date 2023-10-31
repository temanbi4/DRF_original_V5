# Generated by Django 4.2.6 on 2023-10-31 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('payment_amount', models.PositiveIntegerField(verbose_name='Сумма оплаты')),
                ('payment_method', models.CharField(choices=[('Cash', 'Наличные'), ('Transfer', 'Перевод')], max_length=150, verbose_name='Способ оплаты')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.course', verbose_name='оплаченный курс')),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.lesson', verbose_name='оплаченный урок')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'Платеж',
                'verbose_name_plural': 'Платежи',
            },
        ),
    ]
