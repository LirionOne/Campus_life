# Generated by Django 3.2.4 on 2021-06-04 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CampusLife', '0004_auto_20210604_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='salt',
            field=models.TextField(verbose_name='соль'),
        ),
    ]
