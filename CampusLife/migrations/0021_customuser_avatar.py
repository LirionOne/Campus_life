# Generated by Django 3.2.4 on 2021-06-25 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CampusLife', '0020_auto_20210625_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='фото'),
        ),
    ]
