from django.db import models  
class Feedback(models.Model):  
     
    fname = models.CharField(max_length=10)  
    femail = models.EmailField()  
    subject = models.CharField(max_length=15)  
    message = models.CharField(max_length=150)  
    class Meta:  
        db_table = "feedback"  