from django.db import models

# Create your models here.

class Patient(models.Model):
    name= models.CharField(max_length=200)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    country_code=models.CharField(max_length=4)
    phone=models.CharField(max_length=15)
    email=models.EmailField(unique=True)
    address=models.CharField(max_length=1000)
    createdAt=models.DateTimeField(auto_now_add=True)
    