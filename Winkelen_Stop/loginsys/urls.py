from django.urls import path, include
from loginsys import views

urlpatterns = [
    path('',views.index, name="wekleen"),
    path('login_index',views.login_index, ),
    path('registration', views.userreg,name='reg'),
    path('login', views.loginpage,name='loginpage'),
    path('logout', views.logout,name='logout'),
    path('about', views.about,name='about'),
    path('cart', views.cart,name='cart'),
    path('checkout', views.checkout,name='checkout'),
    path('contact', views.contact,name='contact'),
    path('details', views.details,name='details'),
    path('shop', views.shop,name='shop'),
    
]