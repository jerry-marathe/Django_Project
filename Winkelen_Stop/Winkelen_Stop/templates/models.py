from django.db import models


class student(models.Model):
    studentName=models.TextFields();
    studentEmail=models.CharField(max_length=100)
    #To store Image
    avatar=models.ImageField(upload_to="images/")
