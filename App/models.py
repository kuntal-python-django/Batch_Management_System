from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


GENDER_CHOICES =( 
    ("M", "Male"), 
    ("F", "Female"), 
    ("O", "Others"), 
    ("NA", "Prefer Not To Say"), 
) 

GRADE_CHOICES =( 
    (1, "E"), 
    (2, "A+"), 
    (3, "A"), 
    (4, "B+"),
    (5, "B"),
    (6, "C"),
    (7, "NA"), 
)   


class Batch(models.Model):
    batch_id = models.CharField(max_length=10)
    batch_name = models.CharField(max_length=50)
    start_time = models.TimeField(auto_now=False)
    end_time = models.TimeField(auto_now=False)
    is_active = models.BooleanField(default=True)
    batch_start_date = models.DateField(auto_now_add=False)
    batch_end_date = models.DateField(auto_now_add=False)
    batch_url = models.URLField(blank=True, null=True)
    class_video_url = models.TextField()
    attendance_url = models.URLField(blank=True, null=True)
    notice = RichTextUploadingField(default="")
    
    def __str__(self):
        return self.batch_id


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES, default='NA')
    project_submitted = models.BooleanField(default=False)
    grade = models.IntegerField(choices=GRADE_CHOICES, default=7)
    batch = models.ForeignKey(
        Batch,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    
    def __str__(self):
        return self.email


class FeedBack(models.Model):
    name = models.CharField(max_length=50)
    course = models.CharField(max_length=40)
    message = models.TextField()
    country = models.CharField(max_length=20)
    ip = models.GenericIPAddressField(blank=True, null=True)
    browser = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)