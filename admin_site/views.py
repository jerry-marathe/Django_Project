from django.http import HttpResponse
from django.shortcuts import render
from faker import Faker

# Create your views here.


def admin_home(request):
    # return HttpResponse('this is admin site')
    return render(request, 'admin_site/index.html')


# def generatFakeData(request):
#     fake = Faker()
#     for i in range(0, 10):
#         username = fake.username()
#         email = fake.email()
#         pwd = fake.pwd()
#         age = fake.age
#         gender = fake.gender()
#         nationality = fake.nationality()
