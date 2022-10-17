from django import forms  
from sub_category.models import Sub_category  
class Sub_categoryForm(forms.ModelForm):  
    class Meta:  
        model = Sub_category  
        fields = "__all__"  