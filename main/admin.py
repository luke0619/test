from django.contrib import admin
from main import models
# Register your models here.
# Register your models here.
class localadmin(admin.ModelAdmin):
    list_display = ("number","name","year","month","day","temp","RH","Aedes","Culex","Total","time","label",)
    search_fields = ("name",)
    ordering = ("year",)

class testadmin(admin.ModelAdmin):
    list_display = ("name","year","month","day","Aedes","CO2","Culex","PM","RH","temp","number","time","label","Total",)
    search_fields = ("name",)
    ordering = ("year",)

class governadmin(admin.ModelAdmin):
    list_display = ("Locations","City","Year","Week","SO2","CO","O3","PM10","PM25","Nox","No","No2","TEMP","RH","CC",)
    search_fields = ("Locations",)
    ordering = ("id",)
admin.site.register(models.local, localadmin)
admin.site.register(models.test, testadmin)
admin.site.register(models.govern, governadmin)