from django.db import models

# Create your models here.
class Form(models.Model):
    Destination_Name=models.CharField(max_length=30)
    Description=models.CharField(max_length=30)
    Price=models.IntegerField()
    image=models.ImageField(upload_to='sample',default='null.jpg')
