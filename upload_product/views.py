# from django.shortcuts import render,redirect
# from django.contrib import messages
# from .models import Item

# def product_index(request):
#     products = Item.objects.all()
#     context = {'products':products}
#     return render(request, 'upload_products_img/product_index.html', context)

# # Create your views here.
# def addProduct(request):
#     if request.method == "POST":
#         prod = Item()
#         prod.name = request.POST.get('name')
#         prod.description = request.POST.get('description')
#         prod.price = request.POST.get('price')

#         if len(request.FILES) != 0:
#             prod.image = request.FILES['image']

#         prod.save()
#         messages.success(request, "Product Added Successfully")
#         return redirect('/add-product')
#     return render(request, 'upload_products_img/add.html')

from django.shortcuts import render
from .forms import ImageForm


def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'upload_products_img/index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'upload_products_img/index.html', {'form': form})
