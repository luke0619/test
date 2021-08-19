from django.urls import path
from main import views
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from django.contrib import admin
from main import views
from main.views import yolo_detect
app_name = 'main'

urlpatterns = [
    path("", views.main, name='main'),
    path("map/", views.maps, name="map"),
    path("base/", views.base, name="base"),
    path("search/", views.search, name="search"),
    path("data2/", views.data2, name="data2"),
    path("data3/", views.data3, name="data3"),
    path("govern/", views.govern, name="govern"),
    path("introduce1/",views.introduce1, name="introduce1"),
    path("introduce2/",views.introduce2, name="introduce2"),
    path("introduce3/",views.introduce3, name="introduce3"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)