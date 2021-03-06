# Generated by Django 3.1.7 on 2021-04-24 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210412_0009'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='Aedes',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='local',
            name='CO2',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='local',
            name='Culex',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='local',
            name='PM',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='local',
            name='RH',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='local',
            name='temp',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='detection',
            name='lat',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='detection',
            name='lot',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='detection',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='local',
            name='day',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='local',
            name='month',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='local',
            name='name',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='local',
            name='year',
            field=models.CharField(default='', max_length=10),
        ),
    ]
