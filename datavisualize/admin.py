from django.contrib import admin
from .models import DataSet

# Register your models here.
class DataSetAdmin(admin.ModelAdmin):
	list_display=['user','label','value']

admin.site.register(DataSet,DataSetAdmin)