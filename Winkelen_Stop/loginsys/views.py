from django.shortcuts import render,HttpResponse
from django.contrib import messages
from loginsys.models import newuser

# Create your views here.
# def registration(request):
#     return render(request,"registration.html")

def login_index(request):
    return render(request,"login_index.html")

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,'about.html')

def cart(request):
    return render(request,'cart.html')

def checkout(request):
    return render(request,'checkout.html')

def contact(request):
    return render(request,'contact.html')

def details(request):
    return render(request,'details.html')

def shop(request):
    return render(request,'shop.html')

def profile(request):
    return render(request,'profile.html')

def userreg(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['pwd']
        age = request.POST['age']
        # number = request.POST['number']
        gender = request.POST['gender']
        nationality =  request.POST['nationality']
        newuser(username=username,email=email,pwd=pwd,age=age,gender=gender,nationality=nationality).save()
        messages.success(request,'THE NEW USER  ' + request.POST['username'] + ' REGISTER SUCCESSFULLY ADDED..!')
        return render(request,'registration.html')
    else:
        # messages.success('REGISTRATION FAILED..!')
        return render(request,'registration.html')
        
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
    
    if request.method=="POST":
        try:
            userdetails=newuser.objects.get(email=request.POST['email'],pwd=request.POST['pwd'])
            print('username=',userdetails)
            request.session['email'] = userdetails.email
            request.session['username'] = userdetails.username
            request.session['age'] = userdetails.age
            return render(request,'index.html')
        except newuser.DoesNotExist as e:
            messages.success(request,'username / password invalid..!')
    return render(request,'login.html') 


def logout(request):
    try:
        del request.session['email']
    except:
        return render(request,'index.html')
    return render(request,'index.html')