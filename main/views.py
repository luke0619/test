from django.shortcuts import render, redirect
from django.http import HttpResponse

import json
from pyecharts import options as opts
from pyecharts.charts import Bar
from rest_framework.views import APIView
from django.template.context_processors import request
from main import models
from main.models import local, Photo
from calendar import month
from django.shortcuts import redirect
from .forms import UploadModelForm

import numpy as np
import pymysql

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import numpy as np     # 矩阵运算
import urllib          # url解析
import json            # json字符串使用            # opencv包
import os              # 执行操作系统命令
import base64
from django.http import JsonResponse   # json字符串返回


def main(request):
    return render(request, 'main/index.html', locals())

def maps(request):
    data = models.test.objects.last()
    a = models.test.objects.filter(number="1").last()
    b = models.test.objects.filter(number="2").last()
    c = models.test.objects.filter(number="4").last()
    return render(request, 'main/map.html', locals())

def base(request):
    return render(request, 'main/base.html', locals())

def search(request): 
    num1 = range(2021,2022)
    num2 = range(1,13)
    num3 = range(1,32)    
    return render(request, 'main/search.html', locals())

def govern(request):
    num1 = range(2015,2016)
    num2 = range(1,53)    
    return render(request, 'main/govern.html', locals())

def test(request):
    return render(request, 'test.html',locals())

def introduce2(request):
    return render(request, 'main/introduce2.html', locals())

def introduce3(request):
    return render(request, 'main/introduce3.html', locals())
    
def data2(request):
    try:
        year_all = range(2000,2021)
        month_all = range(1,13)
        number = request.GET['location']
        year = request.GET['year']
        month = request.GET['month']
        type = request.GET['type']
        objs = models.test.objects.filter(year=year,month=month,number=number)
        data2 = models.test.objects.filter(number=number).last()
    except:
        message = "test"
    return render(request, 'main/data2.html', locals())    

def data3(request):
    try:
        year_all = range(2000,2021)
        month_all = range(1,13)
        number = request.GET['location']
        year = request.GET['year']
        week1 = request.GET['week1']
        week2 = request.GET['week2']
        type = request.GET['type']
        objs = models.govern.objects.filter(Year=year,id__gte=week1,id__lte=week2,)
    except:
        message = "test4"
    return render(request, 'main/data3.html', locals())    

face_detector = "haarcascade_frontalface_default.xml"  # 默认放置在项目根目录下

@csrf_exempt #增加装饰器，作用是跳过 csrf 中间件的保护
def yolo_detect(request):
    return render(request, 'test.html',locals())

 
def introduce1(request):
    return render(request, 'main/introduce1.html')
    
def read_image(request,stream=None, url=None):
    return render(request, 'test.html',locals())