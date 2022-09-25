from django.db import models  
class Contact(models.Model):  
    cname = models.CharField(max_length=35)  
    cemail = models.EmailField()  
    subject = models.CharField(max_length=50)  
    desc = models.CharField(max_length=200)  
    class Meta:  
        db_table = "contact"  