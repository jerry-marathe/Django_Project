"""wekleen URL Configuration

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
from django.urls import path, include
from user_profile import views as pf 
from loginsys import views
# from loginsys import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('',include('loginsys.urls')),
    # path('cart/',views.cart),
    # path('checkout/',views.checkout),
    # path('contact/',views.contact),
    # path('details/',views.details),
    # path('shop/',views.shop),
    # path('registration/',views.registration),
    # path('loginsys/', include('loginsys.ur/ls')),
    # path('/registration', views.userreg),


    path('profile', pf.profile),  
    path('show',pf.show),  
    path('edit/<int:id>', pf.edit),  
    path('update/<int:id>', pf.update),  
    path('delete/<int:id>', pf.destroy),
]
