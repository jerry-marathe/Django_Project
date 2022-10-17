from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect  
from feedback.forms import FeedbackForm  
from feedback.models import Feedback  
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.  
def feedback(request):  
    if request.method == "POST":  
        form = FeedbackForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                messages.success(request,"Feedback Added Successfully..!!!")
                return redirect('/feedback_show')  
            except:  
                pass  
    else:  
        form = FeedbackForm()  
    return render(request,'feedback_crud/feedback_index.html',{'form':form})  
def feedback_show(request):  
    feedbacks = Feedback.objects.all()  
    paginator = Paginator(feedbacks,4)
    page_num = request.GET.get('page')
    feedback_data_final = paginator.get_page(page_num)
    tatal_page = feedback_data_final.paginator.num_pages
    return render(request,"feedback_crud/feedback_show.html",{'feedbacks':feedbacks, 'feedbacks' : feedback_data_final , 'lastpage' : tatal_page, 'total_page_list' : [n+1 for n in range(tatal_page)]})  
    # return render(request,"feedback_crud/feedback_show.html",{'feedbacks':feedbacks})  
def feedback_edit(request, id):  
    feedback = Feedback.objects.get(id=id)  
    return render(request,'feedback_crud/feedback_edit.html', {'feedback':feedback})  
def feedback_update(request, id):  
    feedback = Feedback.objects.get(id=id)  
    form = FeedbackForm(request.POST, instance = feedback)  
    if form.is_valid():  
        form.save()  
        return redirect("/feedback_show")  
    return render(request, 'feedback_crud/feedback_edit.html', {'feedback': feedback})  
def feedback_destroy(request, id):  
   feedback = Feedback.objects.get(id=id)  
   feedback.delete()  
   return redirect("/feedback_show")