from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard_view (request):
    return render(request, 'main/index.html')

def notice_view (request):
    return render(request, 'main/notice.html')

def event_view (request):
    return render(request, 'main/event.html')

def meeting_view (request):
    return render(request, 'main/meeting.html')

def setting_view (request):
    return render(request, 'main/settings.html')