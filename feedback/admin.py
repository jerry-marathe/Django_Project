from django.contrib import admin

# Register your models here.
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['fname','femail','subject','message']

admin.site.register(Feedback,FeedbackAdmin)