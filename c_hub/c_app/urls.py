from django.urls import path
from .views.main_view import dashboard_view, event_view,notice_view,meeting_view,setting_view
from .views.auth_view import login_view,signup_view

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('event/', event_view, name='event'),
    path('meeting/', meeting_view, name='meeting'),
    path('notice/', notice_view, name='notice'),
    path('setting/', setting_view, name='setting')
]