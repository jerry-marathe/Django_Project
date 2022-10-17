#from unicodedata import sub_category
from django.db import models  
class Sub_category(models.Model):  
    sub_category = models.CharField(max_length=35)  
    
    class Meta:  
        db_table = "sub_category"  