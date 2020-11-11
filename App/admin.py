from django.contrib import admin
from .models import *


class Student_Custom(admin.ModelAdmin):
    search_fields = ['email','name']
    list_display = ['name', 'email', 'mobile', 'gender', 'project_submitted', 'grade', 'batch']
    #list_filter = ['email','name']
    ordering = ('name',)


class Batch_Custom(admin.ModelAdmin):
    search_fields = ['batch_id', 'batch_name']
    list_display = ['batch_name', 'start_time', 'end_time', 'is_active', 'batch_start_date', 'batch_url', 'class_video_url']
    #list_filter = ['batch_id','batch_name']
    ordering = ('batch_name',)


class Feedback_Custom(admin.ModelAdmin):
    list_display = ['name', 'course', 'created_at']
    ordering = ('created_at',)

admin.site.register(Student, Student_Custom)
admin.site.register(Batch, Batch_Custom)
admin.site.register(FeedBack, Feedback_Custom)
