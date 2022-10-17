from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from feedback_webpage.forms import Feedback_webpageForm
from feedback_webpage.models import Feedback_webpage
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.


def feedback_webpage(request):
    if request.method == "POST":
        form = Feedback_webpageForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Feedback Added Successfully..!!!")
                return redirect('/feedback_webpage')
            except:
                pass
    else:
        form = Feedback_webpageForm()
    return render(request, 'winkelen_site/feedback_webpage.html', {'form': form})


def feedback_webpage_show(request):
    feedbacks = Feedback_webpage.objects.all()
    return render(request, "feedback_crud/feedback_webpage_show.html", {'feedbacks': feedbacks})

def feedback_webpage_destroy(request, id):  
   feedback = Feedback_webpage.objects.get(id=id)  
   feedback.delete()  
   return redirect("/feedback_webpage_show")