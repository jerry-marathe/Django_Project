from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from winkelen_stop.models import newuser
from product.models import Product
from image_upload.models import Hotel
from category.models import Category
from sub_category.models import Sub_category
from django.core.paginator import Paginator
from django.views import View
import openpyxl

# Create your views here.


def contact_page(request):
    return render(request, 'winkelen_site/contact_webpage.html')


# Create your views here.
# def registration(request):
#     return render(request,"registration.html")

def login_index(request):
    return render(request, "winkelen_site/login_index.html")


def index(request):
    products = Product.objects.all()
    return render(request, "winkelen_site/index.html", {'product': products})

# def header(request):
#     categorys = Category.objects.all()
#     return render(request,"winkelen_site/header.html",{'categorys':categorys})
    # return render(request,'winkelen_site/header.html')
# class FirstMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)
#         return response


# def upload(request):
#     if "GET" == request.method:
#         return render(request, 'myapp/index.html', {})
#     else:
#         excel_file = request.FILES["excel_file"]

#         # you may put validations here to check extension or file size

#         wb = openpyxl.load_workbook(excel_file)

#         # getting a particular sheet by name out of many sheets
#         worksheet = wb["Sheet1"]
#         print(worksheet)

#         excel_data = list()
#         # iterating over the rows and
#         # getting value from each cell in row
#         for row in worksheet.iter_rows():
#             row_data = list()
#             for cell in row:
#                 row_data.append(str(cell.value))
#             excel_data.append(row_data)

#         return render(request, 'myapp/index.html', {"excel_data": excel_data})


def about(request):
    return render(request, 'winkelen_site/about.html')


def cart(request):
    return render(request, 'winkelen_site/cart.html')

# def category_fetch(request):
#     categorys = Category.objects.all()
#     return render(request,"winkelen_site/header.html",{'categorys':categorys})
    # return render(request,'winkelen_site/cart.html')


def checkout(request):
    return render(request, 'winkelen_site/checkout.html')


def contact(request):
    return render(request, 'winkelen_site/contact.html')


def details(request, detail_id):
    products = Product.objects.get(id=detail_id)
    # products = Product.objects.all()
    return render(request, "winkelen_site/details.html", {'products': products})
    # return render(request,'winkelen_site/details.html')


def shop(request):
    products = Product.objects.all()
    if request.method == "GET":
        pt = request.GET.get('pname')
        if pt != None:
            products = Product.objects.filter(pname__icontains=pt)
            # messages.error(request,"No Product Found..!!! | CheckOut More Products...!!!")
            # return redirect('/shop')
    paginator = Paginator(products, 3)
    page_num = request.GET.get('page')
    product_data_final = paginator.get_page(page_num)
    tatal_page = product_data_final.paginator.num_pages
    return render(request, "winkelen_site/shop.html", {'products': products, 'products': product_data_final, 'lastpage': tatal_page, 'total_page_list': [n+1 for n in range(tatal_page)]})
    # return render(request,"winkelen_site/shop.html",
    # {'product':products})
    # return render(request,'winkelen_site/shop.html')


def profile(request):
    return render(request, 'winkelen_site/profile.html')


def category_webpage(request):
    categorys = Category.objects.all()
    paginator = Paginator(categorys, 4)
    page_num = request.GET.get('page')
    category_data_final = paginator.get_page(page_num)
    tatal_page = category_data_final.paginator.num_pages
    return render(request, "winkelen_site/category_webpage.html", {'categorys': categorys, 'categorys': category_data_final, 'lastpage': tatal_page, 'total_page_list': [n+1 for n in range(tatal_page)]})
    # return render(request,'winkelen_site/category_webpage.html',{'category':categorys})


def sub_category_webpage(request):
    sub_categorys = Sub_category.objects.all()
    paginator = Paginator(sub_categorys, 8)
    page_num = request.GET.get('page')
    sub_category_data_final = paginator.get_page(page_num)
    tatal_page = sub_category_data_final.paginator.num_pages
    return render(request, "winkelen_site/sub_category_webpage.html", {'sub_categorys': sub_categorys, 'sub_categorys': sub_category_data_final, 'lastpage': tatal_page, 'total_page_list': [n+1 for n in range(tatal_page)]})


def image_gallary(request):
    Hotels = Hotel.objects.all()
    return render(request, 'image_gallery_page/display_hotel_images.html')


def userreg(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['pwd']
        age = request.POST['age']
        gender = request.POST['gender']
        nationality = request.POST['nationality']
        newuser(username=username, email=email, pwd=pwd, age=age,
                gender=gender, nationality=nationality).save()
        messages.success(request, 'THE NEW USER  ' +
                         request.POST['username'] + ' REGISTER SUCCESSFULLY ADDED..!')
        return render(request, 'winkelen_site/registration.html')
    else:
        # messages.success('REGISTRATION FAILED..!')
        return render(request, 'winkelen_site/registration.html')


def loginpage(request):
    # if request.method=="POST":
    #     try:
    #         userdetails=newuser.objects.get(email=request.POST['email'],pwd=request.POST['pwd'])
    #         print('username=',userdetails)
    #         request.session['email'] = userdetails.email
    #         request.session['username'] = userdetails.username
    #         request.session['age'] = userdetails.age
    #         return render(request,'index.html')
    #     except newuser.DoesNotExist as e:
    #         messages.success(request,'username / password invalid..!')
    # return render(request,'login.html')

    if request.method == "POST":
        try:
            userdetails = newuser.objects.get(
                email=request.POST['email'], pwd=request.POST['pwd'])
            print('username=', userdetails)
            request.session['email'] = userdetails.email
            request.session['username'] = userdetails.username
            request.session['age'] = userdetails.age
            return render(request, 'winkelen_site/index.html')
        except newuser.DoesNotExist as e:
            messages.success(request, 'username / password invalid..!')
    return render(request, 'winkelen_site/login.html')


def logout(request):
    try:
        del request.session['email']
    except:
        return render(request, 'winkelen_site/index.html')
    return render(request, 'winkelen_site/index.html')


class Cart_1(View):
    def post(self, request):
        product = request.POST.get('product')
        print(product)
        return redirect('/shop')

    def get(self, request):
        product = None
        categories = Category.get_all_Categories()

        categoryID = request.GET.get('category')
