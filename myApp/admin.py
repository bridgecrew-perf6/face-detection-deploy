from django.contrib import admin
from  django.contrib.auth.models  import  Group

from myApp.models import FaceRecognition

# Register your models here.

admin.site.unregister(Group)

class  FaceRecognitionAdmin(admin.ModelAdmin):
    list_display=('id', 'record_date', 'image_tag')

    list_filter = ['record_date',]

    search_fields = ['record_date']

    exclude = ('id',)


admin.site.register(FaceRecognition, FaceRecognitionAdmin)