from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *

# Create your views here.


def profile_image_view(request):

    if request.method == 'POST':
        form = Profile_webForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                form.save()
                return redirect('/profile')
            except:
                pass
    else:
        form = Profile_webForm()
    return render(request, 'winkelen_site/profile.html', {'form': form})


def upload_profile_image(request):
    return render(request, 'winkelen_site/profile_img.html')


# Python program to view
# for displaying images


# def display_profile_images(request):

#     if request.method == 'GET':

#         Profile_webs = Profile_web.objects.all()
#         return render(request, 'winkelen_site/profile.html', {'Profile_web': Profile_webs})
