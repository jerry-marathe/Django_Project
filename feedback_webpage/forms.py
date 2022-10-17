from django import forms
from feedback_webpage.models import Feedback_webpage


class Feedback_webpageForm(forms.ModelForm):
    class Meta:
        model = Feedback_webpage
        fields = "__all__"
