from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from category.forms import CategoryForm
from category.models import Category
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
import csv
import datetime


def category(request):

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(
                    request, "Category Details Added Successfully..!!!")
                return redirect('/category_show')
            except:
                pass
    else:
        form = CategoryForm()
    return render(request, 'category_crud/category_index.html', {'form': form})


def category_show(request):
    categorys = Category.objects.all()
    paginator = Paginator(categorys, 4)
    page_num = request.GET.get('page')
    category_data_final = paginator.get_page(page_num)
    tatal_page = category_data_final.paginator.num_pages
    return render(request, "category_crud/category_show.html", {'categorys': categorys, 'categorys': category_data_final, 'lastpage': tatal_page, 'total_page_list': [n+1 for n in range(tatal_page)]})
    # return render(request,"category_crud/category_show.html",{'categorys':categorys})


def category_edit(request, id):
    category = Category.objects.get(id=id)
    return render(request, 'category_crud/category_edit.html', {'category': category})


def category_update(request, id):
    category = Category.objects.get(id=id)
    form = CategoryForm(request.POST, instance=category)
    if form.is_valid():
        form.save()
        return redirect("/category_show")
    return render(request, 'category_crud/category_edit.html', {'category': category})


def category_destroy(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect("/category_show")


def category_export_csv(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Expenses' + \
        str(datetime.datetime.now()) + '.csv'

    writer = csv.writer(response)
    writer.writerow(['Category Name'])

    # reports = Report.objects.filter(rname=request.user)
    categorys = Category.objects.all()

    for category in categorys:
        writer.writerow([category.category])

    return response
