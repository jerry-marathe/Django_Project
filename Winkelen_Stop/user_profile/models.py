from django.db import models  
class Profile(models.Model):  
    full_name = models.CharField(max_length=20)  
    user_name = models.CharField(max_length=20)  
    user_email = models.EmailField()  
    curr_pass = models.CharField(max_length=15)  
    new_pass = models.CharField(max_length=15)  
    con_pass = models.CharField(max_length=15)  
    class Meta:  
        db_table = "profile"  