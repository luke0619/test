# Generated by Django 3.1.7 on 2021-08-19 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_govern_month'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='govern',
            name='Month',
        ),
    ]
