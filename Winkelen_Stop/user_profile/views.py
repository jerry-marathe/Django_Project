from django.shortcuts import render, redirect,  HttpResponse 
from user_profile.forms import ProfileForm  
from user_profile.models import Profile  
# Create your views here.  
def profile(request):  
    if request.method == "POST":  
        form = ProfileForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show_profile')  
            except:  
                pass  
    else:  
        form = ProfileForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    profiles = Profile.objects.all()  
    return render(request,"show.html",{'profiles':profiles})  
def edit(request, id):  
    profile = Profile.objects.get(id=id)  
    return render(request,'edit.html', {'profile':profile})  
def update(request, id):  
    profile = Profile.objects.get(id=id)  
    form = ProfileForm(request.POST, instance = profile)  
    if form.is_valid():  
        form.save()  
        return redirect("/show_profile")  
    return render(request, 'edit.html', {'profile': profile})  
def destroy(request, id):  
    profile = Profile.objects.get(id=id)  
    profile.delete()  
    return redirect("/show_profile")
def home(request):
    return HttpResponse("this is home page")
