from django.db import models

# Create your models here.
class InsertData(models.Model):
    firstname=models.CharField(max_length=200)
    secondname=models.CharField(max_length=200)
    thirdname=models.CharField(max_length=200)