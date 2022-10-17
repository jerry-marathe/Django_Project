from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def hotel_image_view(request):

	if request.method == 'POST':
		form = HotelForm(request.POST, request.FILES)

		if form.is_valid():
			try:
				form.save()
				return redirect('/admin_site')
			except:
				pass
	else:
		form = HotelForm()
	return render(request, 'image_gallery_page/hotel_image_form.html', {'form' : form})


def success(request):
	return HttpResponse('successfully uploaded')

# Python program to view
# for displaying images

def display_hotel_images(request):

	if request.method == 'GET':

		Hotels = Hotel.objects.all()
		return render(request, 'image_gallery_page/display_hotel_images.html',{'hotel_images' : Hotels})
