from django.db import models

# Create your models here.
# models.py


class Profile_web(models.Model):
    profile_Main_Img = models.ImageField(upload_to='profile_images/')
