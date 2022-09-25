"""crudexample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  
from django.urls import path  
from employee import views as ev 
from contact import views as cv  
from feedback import views as fb  

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('emp', ev.emp),  
    path('show',ev.show),  
    path('home',ev.home),  
    path('edit/<int:id>', ev.edit),  
    path('update/<int:id>', ev.update),  
    path('delete/<int:id>', ev.destroy),  

 
    path('contact', cv.contact),  
    path('contact_show',cv.contact_show),  
    # path('contact_edit/<int:id>', cv.contact_edit),  
    # path('contact_update/<int:id>', cv.contact_update),  
    path('contact_delete/<int:id>', cv.contact_destroy),  


    
    path('feedback', fb.feedback),  
    path('feedback_show',fb.feedback_show),  
    # path('feedback_edit/<int:id>', fb.feedback_edit),  
    # path('feedback_update/<int:id>', fb.feedback_update),  
    path('delete/<int:id>', fb.feedback_destroy),  
]  
