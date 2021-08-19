from django.db import models
from django.utils import timezone
from pdb import pm
# Create your models here.
class local(models.Model):
    name = models.CharField(max_length=10, null=False, default='')
    year = models.CharField(max_length=10, null=False, default='')
    month = models.CharField(max_length=10, null=False, default='')
    day = models.CharField(max_length=10, null=False, default='')
    temp = models.CharField(max_length=10, null=False, default='')
    RH = models.CharField(max_length=10, null=False, default='')
    Aedes = models.CharField(max_length=10, null=False, default='0')
    Culex = models.CharField(max_length=10, null=False, default='0')
    Total = models.CharField(max_length=10, null=False, default='0')
    number = models.CharField(max_length=10, null=False, default='1')
    time = models.DateTimeField('回傳日期',default = timezone.now)
    label = models.CharField(max_length=5, null=False, default='')
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    def __str__(self):
        return self.name

class Photo(models.Model):
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    upload_date = models.DateField(default=timezone.now)

class test(models.Model):
    CO2 = models.CharField(max_length=10, null=False, default='')
    PM = models.CharField(max_length=10, null=False, default='')
    RH = models.CharField(max_length=10, null=False, default='')
    name = models.CharField(max_length=10, null=False, default='')
    year = models.CharField(max_length=10, null=False, default='')
    month = models.CharField(max_length=10, null=False, default='')
    day = models.CharField(max_length=10, null=False, default='')
    temp = models.CharField(max_length=10, null=False, default='')
    RH = models.CharField(max_length=10, null=False, default='')
    Aedes = models.CharField(max_length=10, null=False, default='0')
    Culex = models.CharField(max_length=10, null=False, default='0')
    Total = models.CharField(max_length=10, null=False, default='0')
    number = models.CharField(max_length=10, null=False, default='1')
    time = models.DateTimeField('回傳日期',default = timezone.now)
    label = models.CharField(max_length=5, null=False, default='')
    def __str__(self):
        return self.name

class govern(models.Model):
    id = models.CharField(max_length=20, null=False, default='',primary_key = True)
    Locations =  models.CharField(max_length=20, null=False, default='')
    City = models.CharField(max_length=20, null=False, default='')
    Year = models.CharField(max_length=20, null=False, default='')
    Week = models.CharField(max_length=20, null=False, default='')
    SO2 = models.CharField(max_length=20, null=False, default='')
    CO = models.CharField(max_length=20, null=False, default='')
    O3 = models.CharField(max_length=20, null=False, default='')
    PM10 = models.CharField(max_length=20, null=False, default='')
    PM25 = models.CharField(max_length=20, null=False, default='')
    Nox = models.CharField(max_length=20, null=False, default='')
    No = models.CharField(max_length=20, null=False, default='')
    No2 = models.CharField(max_length=20, null=False, default='')
    TEMP = models.CharField(max_length=20, null=False, default='')
    RH = models.CharField(max_length=20, null=False, default='')
    CC = models.CharField(max_length=20, null=False, default='')