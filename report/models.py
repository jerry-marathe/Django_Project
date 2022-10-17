from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
from django.db import models  
class Report(models.Model):  

    rname = models.CharField(max_length=10)  
    rsubject = models.CharField(max_length=15)  
    message = models.CharField(max_length=150)  
    class Meta:  
        db_table = "report"  