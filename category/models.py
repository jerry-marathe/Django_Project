from unicodedata import category
from django.db import models  
class Category(models.Model):  
    category = models.CharField(max_length=35)  
    
    class Meta:  
        db_table = "category"  