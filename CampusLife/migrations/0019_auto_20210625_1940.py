# Generated by Django 3.2.4 on 2021-06-25 09:40

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('CampusLife', '0018_auto_20210624_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('birthday', models.DateField(null=True, verbose_name='День рождения')),
                ('course', models.CharField(max_length=1, verbose_name='Курс')),
                ('inform', models.TextField(verbose_name='Информация о себе')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='фото')),
                ('gender', models.CharField(choices=[('Мужчина', 'Мужчина'), ('Женщина', 'Женщина')], default='Мужчина', max_length=7, verbose_name='Пол')),
            ],
            options={
                'verbose_name': 'ПОльзователь',
                'verbose_name_plural': 'Пользователи',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='event_img',
            field=models.ImageField(blank=True, upload_to='C:/media/event_images', verbose_name='изображение для события'),
        ),
    ]
