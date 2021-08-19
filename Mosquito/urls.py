from django.contrib import admin
from django.urls import path,include, re_path
from main import views

from django.conf.global_settings import MEDIA_ROOT
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from main.views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url
from main.views import main,yolo_detect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls', namespace='main')),
    url(r'^yolo_detect/$', yolo_detect, name='yolo_detect'),  
    re_path('.*', views.main),
]
