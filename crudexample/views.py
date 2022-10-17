from django.shortcuts import render, HttpResponse

def contact_crud(request):
    return render(request,'contact_page.html')
    # return HttpResponse("this is contact crud")