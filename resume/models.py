from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from uaclient.util import retry

# Create your models here.

free=[('Available','A'),('Unavailable','U')]
num=[('first','f'),('second','s'),('third','t')]
class About(models.Model):
    name=models.CharField(max_length=30)
    birthday=models.DateTimeField(default=None)
    degree=models.CharField(max_length=30)
    experience=models.IntegerField()
    phone=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=50)
    freelance=models.CharField(max_length=50,choices=free)
    text=HTMLField()
    photo_me=models.ImageField(null=True,blank=True,upload_to="image/")

    def __str__(self):
        return self.name

class Education(models.Model):
    degree_in=models.CharField(max_length=50)
    University=models.CharField(max_length=50)
    year=models.CharField(max_length=30)
    text=HTMLField()

    def __str__(self):
        return self.University

class Expericence(models.Model):
    skill=models.CharField(max_length=25)
    company=models.CharField(max_length=25)
    year=models.CharField(max_length=15)
    text=HTMLField()

    def __str__(self):
        return self.skill

class Services(models.Model):
    skill=models.CharField(max_length=30)
    icon=models.CharField(max_length=30)
    text=HTMLField()

    def __str__(self):
        return self.skill

class Gallery(models.Model):
    image=models.ImageField(null=True,blank=True,upload_to="image/")
    position = models.CharField(max_length=50, choices=num,default='f')

class Client(models.Model):
    client_name=models.CharField(max_length=50)
    client_image=models.ImageField(null=True,blank=True,upload_to="image/")
    client_message=HTMLField()

    def __str__(self):
        return self.client_name

class Blog(models.Model):
    blog_image=models.ImageField(null=True,blank=True,upload_to="image/")
    blog_date=models.DateTimeField()
    blog_text=HTMLField()

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    text=HTMLField()

    def __str__(self):
        return self.name

class Skill(models.Model):
    skill=models.CharField(max_length=30)
    skill_percentage=models.IntegerField()
    color=models.CharField(max_length=30)

    def __str__(self):
        return self.skill