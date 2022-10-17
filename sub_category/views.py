from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from sub_category.forms import Sub_categoryForm
from sub_category.models import Sub_category
from django.contrib import messages
from django.http import HttpResponse
import csv
import datetime
from django.core.paginator import Paginator


def sub_category(request):

    if request.method == "POST":
        form = Sub_categoryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(
                    request, "Sub_category Details Added Successfully..!!!")
                return redirect('/sub_category_show')
            except:
                pass
    else:
        form = Sub_categoryForm()
    return render(request, 'sub_category_crud/sub_category_index.html', {'form': form})


def sub_category_show(request):
    sub_categorys = Sub_category.objects.all()
    paginator = Paginator(sub_categorys, 4)
    page_num = request.GET.get('page')
    sub_category_data_final = paginator.get_page(page_num)
    tatal_page = sub_category_data_final.paginator.num_pages
    return render(request, "sub_category_crud/sub_category_show.html", {'sub_categorys': sub_categorys, 'sub_categorys': sub_category_data_final, 'lastpage': tatal_page, 'total_page_list': [n+1 for n in range(tatal_page)]})
    # return render(request,"sub_category_crud/sub_category_show.html",{'sub_categorys':sub_categorys})


def sub_category_edit(request, id):
    sub_category = Sub_category.objects.get(id=id)
    return render(request, 'sub_category_crud/sub_category_edit.html', {'sub_category': sub_category})


def sub_category_update(request, id):
    sub_category = Sub_category.objects.get(id=id)
    form = Sub_categoryForm(request.POST, instance=sub_category)
    if form.is_valid():
        form.save()
        return redirect("/sub_category_show")
    return render(request, 'sub_category_crud/sub_category_edit.html', {'sub_category': sub_category})


def sub_category_destroy(request, id):
    sub_category = Sub_category.objects.get(id=id)
    sub_category.delete()
    return redirect("/sub_category_show")


def sub_category_export_csv(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Expenses' + \
        str(datetime.datetime.now()) + '.csv'

    writer = csv.writer(response)
    writer.writerow(['Sub Category Name'])

    # reports = Report.objects.filter(rname=request.user)
    sub_categorys = Sub_category.objects.all()

    for sub_category in sub_categorys:
        writer.writerow([sub_category.sub_category])

    return response
