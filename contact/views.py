from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect  
from contact.forms import ContactForm  
from contact.models import Contact  
from django.contrib import messages
from django.core.paginator import Paginator
def contact(request):  

    if request.method == "POST":  
        form = ContactForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()
                messages.success(request,"Contact Details Added Successfully..!!!")  
                return redirect('/contact_show')  
            except:  
                pass  
    else:  
        form = ContactForm()  
    return render(request,'contact_crud/contact_index.html',{'form':form})  
def contact_show(request):  
    contacts = Contact.objects.all() 
    paginator = Paginator(contacts,4)
    page_num = request.GET.get('page')
    contact_data_final = paginator.get_page(page_num)
    tatal_page = contact_data_final.paginator.num_pages
    # data={
    #     'contacts' : contact_data_final,
    # } 
    return render(request,"contact_crud/contact_show.html",{'contacts':contacts, 'contacts' : contact_data_final , 'lastpage' : tatal_page, 'total_page_list' : [n+1 for n in range(tatal_page)]})  
def contact_edit(request, id):  
    contact = Contact.objects.get(id=id)  
    return render(request,'contact_crud/contact_edit.html', {'contact':contact})  
def contact_update(request, id):  
    contact = Contact.objects.get(id=id)  
    form = ContactForm(request.POST, instance = contact)  
    if form.is_valid():  
        form.save()  
        return redirect("/contact_show")  
    return render(request, 'contact_crud/contact_edit.html', {'contact': contact})  
def contact_destroy(request, id):  
    contact = Contact.objects.get(id=id)  
    contact.delete()  
    return redirect("/contact_show") 

