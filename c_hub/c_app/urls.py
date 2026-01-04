from django.urls import path
from .views.main_view import dashboard_view, event_view, notice_view, meeting_view, setting_view
from .views.auth_view import login_view, signup_view

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('event/', event_view, name='event'),
    path('meeting/', meeting_view, name='meeting'),
    path('setting/', setting_view, name='setting'),
    
    # URL for creating or editing a notice (when no ID is provided, it's create, when an ID is provided, it's edit)
    path('notice/', notice_view, name='create_notice'),  # This is for creating a notice
    path('notice/<int:notice_id>/', notice_view, name='edit_notice'),  # This is for editing a notice
]
