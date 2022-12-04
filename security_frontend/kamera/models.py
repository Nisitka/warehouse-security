from django.db import models

# Create your models here.
class Cars(models.Model):
    number = models.CharField(max_length=20)
    owner = models.CharField(max_length=30)

class People(models.Model):
    image = models.ImageField(upload_to='kamera/images')
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)