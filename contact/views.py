from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect  
from contact.forms import ContactForm  
from contact.models import Contact  
# Create your views here.  
def contact(request):  
    if request.method == "POST":  
        form = ContactForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/contact_show')  
            except:  
                pass  
    else:  
        form = ContactForm()  
    return render(request,'index.html',{'form':form})  
def contact_show(request):  
    contacts = Contact.objects.all()  
    return render(request,"show.html",{'contacts':contacts})  
# def contact_edit(request, id):  
#     contact = Contact.objects.get(id=id)  
#     return render(request,'edit.html', {'contact':contact})  
def contact_update(request, id):  
    contact = Contact.objects.get(id=id)  
    form = ContactForm(request.POST, instance = contact)  
    if form.is_valid():  
        form.save()  
        return redirect("/contact_show")  
    return render(request, 'edit.html', {'contact': contact})  
def contact_destroy(request, id):  
    contact = Contact.objects.get(id=id)  
    contact.delete()  
    return redirect("/contact_show") 