# Generated by Django 3.1.7 on 2021-05-10 08:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210510_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='儲存日期'),
        ),
    ]