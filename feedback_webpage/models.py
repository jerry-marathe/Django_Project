from django.db import models


class Feedback_webpage(models.Model):
    rate = models.IntegerField()
    email = models.CharField(max_length=150)
    msg = models.CharField(max_length=150)

    class Meta:
        db_table = "feedback_webpage"
