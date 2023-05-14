from django.contrib import admin
from .models import *
from embed_video.admin import AdminVideoMixin
from .models import Item

# Register your models here.

admin.site.register(Products)

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass
admin.site.register(Item,MyModelAdmin)