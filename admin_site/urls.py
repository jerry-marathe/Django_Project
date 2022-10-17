from admin_site import views
from django.urls import path 

urlpatterns = [
    path('admin_site_index/',views.admin_home),
    # path('generaterFakeData/',generateFakeData,name='generateFakeDate')
]