from django.db import models 


class Product(models.Model):  
    pid = models.CharField(max_length=20)  
    pname = models.CharField(max_length=20)  
    rate = models.CharField(max_length=15)  
    desc = models.CharField(max_length=50)  
    product_Main_img = models.ImageField(upload_to='images/')
    class Meta:  
        db_table = "product"  