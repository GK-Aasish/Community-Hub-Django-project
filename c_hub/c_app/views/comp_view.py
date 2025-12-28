from django.shortcuts import render

def notice_view (request):
    return render(request, 'components/notice.html')

def event_view (request):
    return render(request, 'component/event.html')

def meeting_view (request):
    return render(request, 'component/meeting.html')