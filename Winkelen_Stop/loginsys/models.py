from django.db import models

# Create your models here.


class newuser(models.Model):
    username = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    pwd = models.CharField(max_length=150)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    nationality = models.CharField(max_length=150)