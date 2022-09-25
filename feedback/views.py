from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect  
from feedback.forms import FeedbackForm  
from feedback.models import Feedback  
# Create your views here.  
def feedback(request):  
    if request.method == "POST":  
        form = FeedbackForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/feedback_show')  
            except:  
                pass  
    else:  
        form = FeedbackForm()  
    return render(request,'index.html',{'form':form})  
def feedback_show(request):  
    feedbacks = Feedback.objects.all()  
    return render(request,"show.html",{'feedbacks':feedbacks})  
# def edit(request, id):  
#     feedback = Feedback.objects.get(id=id)  
#     return render(request,'edit.html', {'feedback':feedback})  
# def update(request, id):  
#     feedback = Feedback.objects.get(id=id)  
#     form = FeedbackForm(request.POST, instance = feedback)  
#     if form.is_valid():  
#         form.save()  
#         return redirect("/feedback_show")  
#     return render(request, 'edit.html', {'feedback': feedback})  
def feedback_destroy(request, id):  
   feedback = Feedback.objects.get(id=id)  
   feedback.delete()  
   return redirect("/feedback_show")