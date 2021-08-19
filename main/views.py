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

import cv2
import numpy as np
import pymysql

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import numpy as np     # 矩阵运算
import urllib          # url解析
import json            # json字符串使用
import cv2             # opencv包
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
    default = {"safely executed": False} #初始未执行
    net=cv2.dnn.readNet('Mosquito/yolov4.weights','Mosquito/yolov4.cfg','darknet')
    layer_names=net.getLayerNames()
    output_layers=[layer_names[i[0]-1] for i in net.getUnconnectedOutLayers()]
    classes=[line.strip() for line in open('Mosquito/family.names')]
    colors=[(0,0,255),(255,0,0),(0,255,0)]
    #规定客户端使用POST请求上传检测图片
    if request.method == "POST":
        if request.FILES.get('image') is not None: #请求中包含图像则以流形式读取图像
            image_to_read = read_image(stream = request.FILES["image"])
            
        else: # 返回错误说明
            default["error_value"] = "提交格式错误，无法解析到image图像"
            return JsonResponse(default)
        img=cv2.resize(image_to_read, (800,600),interpolation=cv2.INTER_CUBIC)
        height, width, channels=img.shape
        blob=cv2.dnn.blobFromImage(img,1/255.0,(416,416),(0,0,0),True, crop=False)
        net.setInput(blob)
        outs=net.forward(output_layers)
    
        class_ids=[]
        confidences=[]
        boxes=[]
        for out in outs:
            for detection in out:
                tx, ty, tw, th, confidence=detection[0:5]
                scores=detection[5:]
                class_id=np.argmax(scores)
                if confidence > 0.6:                    
                    center_x=int(tx*width)
                    center_y=int(ty*height)
                    w=int(tw*width)
                    h=int(th*height)
                    x=int(center_x-w / 2)
                    y=int(center_y-h / 2)
                    boxes.append([x,y,w,h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)        
        indexes=cv2.dnn.NMSBoxes(boxes,confidences,0.2,0.3)
        font=cv2.FONT_HERSHEY_PLAIN
        Culex,Aedes =(0,0)
        for i in range(len(boxes)):
            if i in indexes:
                x,y,w,h=boxes[i]
                label=str(classes[class_ids[i]])          
                if str(classes[class_ids[i]]) == "Aedes":
                    Aedes += 1
                if str(classes[class_ids[i]]) == "Culex":
                    Culex += 1
                color=colors[class_ids[i]%2]
                cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
                cv2.putText(img,label,(x,y-5), font, 2, color,1)
        
        cv2.putText(img,'No. of Aedes:'+str(Aedes),(0,50), cv2.FONT_HERSHEY_DUPLEX, 1, (255,0,255),1)
        cv2.putText(img,'No. of Culex:'+str(Culex),(0,100), cv2.FONT_HERSHEY_DUPLEX, 1, (255,0,255),1)
        
        retval, buffer_img= cv2.imencode('.jpg', img) #在内存中编码为jpg格式
        
        img64 = base64.b64encode(buffer_img) #base64编码转换用于网络传输
        img64=str(img64, encoding='utf-8') #bytes转换为str类型
        default["img64"] = img64  #json封装
    return JsonResponse(default)

 
def introduce1(request):
    return render(request, 'main/introduce1.html')
    
def read_image(stream=None, url=None):
 
    if url is not None:
        response = urllib.request.urlopen(url)
        data_temp = response.read()
 
    elif stream is not None:
        data_temp = stream.read()
 
    image = np.asarray(bytearray(data_temp), dtype="uint8")
    
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image