from django.shortcuts import render

def dashboard_view (request):
    return render(request, 'main/index.html')

def notice_view (request):
    return render(request, 'main/notice.html')

def event_view (request):
    return render(request, 'main/event.html')

def meeting_view (request):
    return render(request, 'main/meeting.html')