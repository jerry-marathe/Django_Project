from django.shortcuts import render, redirect  
from product.forms import ProductForm  
from product.models import Product  
from .forms import *
# Create your views here.  
def product(request):  
    if request.method == "POST":  
        form = ProductForm(request.POST ,request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/product_show')  
            except:  
                pass  
    else:  
        form = ProductForm()  
    return render(request,'product_crud/product_index.html',{'form':form})  
def product_show(request):  
    if request.method == 'GET':
        products = Product.objects.all()  
        return render(request,"product_crud/product_show.html",{'products':products})  
def product_edit(request, id):  
    product = Product.objects.get(id=id)  
    return render(request,'product_crud/product_edit.html', {'product':product})  
def product_update(request, id):  
    product = Product.objects.get(id=id)  
    form = ProductForm(request.POST, instance = product)  
    if form.is_valid():  
        form.save()  
        return redirect("/product_show")  
    return render(request, 'product_crud/product_edit.html', {'product': product})  
def product_destroy(request, id):  
    product = Product.objects.get(id=id)  
    product.delete()  
    return redirect("/product_show")