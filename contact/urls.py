from django.urls import path
from contact import views as cv

urlpatterns = [
    path('contact', cv.contact),  
    path('contact_show',cv.contact_show),  
    path('contact_edit/<int:id>', cv.contact_edit),  
    path('contact_update/<int:id>', cv.contact_update),  
    path('contact_delete/<int:id>', cv.contact_destroy),  
]