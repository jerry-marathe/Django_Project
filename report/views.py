from datetime import datetime
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from report.forms import ReportForm
from report.models import Report
from django.contrib import messages
from django.http import HttpResponse
import csv
import datetime
# Create your views here.


def report(request):
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(
                    request, "Contact Details Added Successfully..!!!")
                return redirect('/report_show')
            except:
                pass
    else:
        form = ReportForm()
    return render(request, 'report_curd/report_index.html', {'form': form})


def report_show(request):
    reports = Report.objects.all()
    return render(request, "report_curd/report_show.html", {'reports': reports})


def report_edit(request, id):
    report = Report.objects.get(id=id)
    return render(request, 'report_curd/report_edit.html', {'report': report})


def report_update(request, id):
    report = Report.objects.get(id=id)
    form = ReportForm(request.POST, instance=report)
    if form.is_valid():
        form.save()
        return redirect("/report_show")
    return render(request, 'report_curd/report_edit.html', {'report': report})


def report_destroy(request, id):
    report = Report.objects.get(id=id)
    report.delete()
    return redirect("/report_show")


def report_export_csv(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Expenses' + \
        str(datetime.datetime.now()) + '.csv'

    writer = csv.writer(response)
    writer.writerow(['Report Name', 'Subject', 'Message'])

    # reports = Report.objects.filter(rname=request.user)
    reports = Report.objects.all()

    for report in reports:
        writer.writerow([report.rname, report.rsubject, report.message])

    return response
