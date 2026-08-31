from django.db import models

# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length=200)
    specialization=models.CharField(max_length=100)
    country_code=models.CharField(max_length=4)
    phone=models.CharField(max_length=15)
    email=models.EmailField(unique=True)
    createdAt=models.DateTimeField(auto_now_add=True)

    