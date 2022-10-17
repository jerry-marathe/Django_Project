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
from winkelen_stop import views as webv
from sub_category import views as sct
from category import views as ct
from admin_site import views as adv
from report import views as rp
from product import views as pd
from feedback_webpage import views as fbwb
from feedback import views as fb
from contact import views as cv
from employee import views as ev
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from image_upload import views as upv
from profile_web import views as piu

# from bags import views as bg

urlpatterns = [

    path('', webv.index),
    path('login_index', webv.login_index, ),
    path('registration', webv.userreg, name='reg'),
    path('login', webv.loginpage, name='loginpage'),
    path('logout', webv.logout, name='logout'),
    path('about', webv.about, name='about'),
    path('cart', webv.cart, name='cart'),
    path('checkout', webv.checkout, name='checkout'),
    path('contact_page', webv.contact),
    path('details/<detail_id>', webv.details, name='details'),
    path('shop/', webv.shop, name='shop'),
    path('profile', webv.profile, name='profile'),
    # path('header_page',webv.header),
    path('category_webpage/', webv.category_webpage),
    path('sub_category_webpage/', webv.sub_category_webpage),
    

    path('', webv.Cart_1.as_view(), name=''),
    path('admin/', admin.site.urls),
    path('emp', ev.emp),
    path('show', ev.show),
    path('home', ev.home),
    path('edit/<int:id>', ev.edit),
    path('update/<int:id>', ev.update),
    path('delete/<int:id>', ev.destroy),

    path('admin_site', adv.admin_home),

    path('image_upload', upv.hotel_image_view, name='image_upload'),
    path('success', upv.success, name='success'),
    path('images', upv.display_hotel_images, name='hotel_images'),
    # path('upload_images', upv.upload_hotel_images, name = 'hotel_images'),

    # path('add-product/',upv.addProduct,name="add-prod"),
    # path('upload/', upv.image_upload_view),

    path('contact', cv.contact),
    path('contact_show/', cv.contact_show),
    path('contact_edit/<int:id>', cv.contact_edit),
    path('contact_update/<int:id>', cv.contact_update),
    path('contact_delete/<int:id>', cv.contact_destroy),



    path('profile_image_upload', piu.profile_image_view,
         name='profile_image_upload'),
    #path('profile_images', piu.display_profile_images, name='profile_images'),

    path('upload_profile_image', piu.upload_profile_image,
         name='upload_profile_image'),

    path('feedback', fb.feedback),
    path('feedback_show/', fb.feedback_show),
    path('feedback_edit/<int:id>', fb.feedback_edit),
    path('feedback_update/<int:id>', fb.feedback_update),
    path('feedback_delete/<int:id>', fb.feedback_destroy),

    path('feedback_webpage', fbwb.feedback_webpage),
    path('feedback_webpage_show/', fbwb.feedback_webpage_show),
    path('feedback_webpage_delete/<int:id>', fbwb.feedback_webpage_destroy),

    # path('jeans', cg.jeans),
    # path('jeans_show',cg.jeans_show),
    # # path('feedback_edit/<int:id>', fb.feedback_edit),
    # # path('feedback_update/<int:id>', fb.feedback_update),
    # path('delete/<int:id>', cg.jeans_destroy),


    path('product', pd.product),
    path('product_show', pd.product_show),
    path('product_edit/<int:id>', pd.product_edit),
    path('product_update/<int:id>', pd.product_update),
    path('product_delete/<int:id>', pd.product_destroy),

    path('report', rp.report),
    path('report_show', rp.report_show),
    path('report_edit/<int:id>', rp.report_edit),
    path('report_update/<int:id>', rp.report_update),
    path('report_delete/<int:id>', rp.report_destroy),
    path('report_export_csv/', rp.report_export_csv),




    path('category', ct.category),
    path('category_show/', ct.category_show),
    path('category_edit/<int:id>', ct.category_edit),
    path('category_update/<int:id>', ct.category_update),
    path('category_delete/<int:id>', ct.category_destroy),
    path('category_export_csv/', ct.category_export_csv),

    path('sub_category', sct.sub_category),
    path('sub_category_show/', sct.sub_category_show),
    path('sub_category_edit/<int:id>', sct.sub_category_edit),
    path('sub_category_update/<int:id>', sct.sub_category_update),
    path('sub_category_delete/<int:id>', sct.sub_category_destroy),
    path('sub_category_export_csv/', sct.sub_category_export_csv),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
