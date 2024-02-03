from django.shortcuts import render, redirect, loader
from django.contrib.auth.decorators import login_required
from .models import TimesheetEntry
from .forms import TimesheetForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, settings
from django.http import HttpResponse



def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('timesheet_list')  # Điều hướng sau khi đăng ký thành công, bạn có thể thay đổi theo ý muốn.
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


# @login_required(login_url="/timesheet/timesheet.html" + settings.QT_LOGIN)
# def my_entries(request):
#     template = loader.get_template("timesheet/timesheet.html")
#     context = {}
#     return HttpResponse(template.render(context, request))
@login_required
def timesheet_list(request):
    timesheet_entries = TimesheetEntry.objects.filter(user=request.user)
    return render(request, 'timesheet/timesheet_list.html', {'timesheet_entries': timesheet_entries})

@login_required
def add_timesheet_entry(request):
    if request.method == 'POST':
        form = TimesheetForm(request.POST)
        if form.is_valid():
            timesheet_entry = form.save(commit=False)
            timesheet_entry.user = request.user
            timesheet_entry.save()
            return redirect('timesheet_list')
    else:
        form = TimesheetForm()
    return render(request, 'timesheet/add_timesheet_entry.html', {'form': form})