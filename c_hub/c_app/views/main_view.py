from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Notices
from django.contrib import messages


@login_required
def dashboard_view (request):
    return render(request, 'main/index.html')

@login_required
def notice_view(request, notice_id=None):  # notice_id is optional for editing
    errors = {}
    mode = 'create' if notice_id is None else 'edit'

    # If in edit mode, retrieve the existing notice
    if mode == 'edit':
        notice = get_object_or_404(Notices, id=notice_id, author=request.user)
    else:
        notice = None  # Creating a new notice, so no notice object
    
    # Handling POST request for both create and edit
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        description = request.POST.get('description')

        # Validate the data
        if not title:
            errors['title'] = "Title is required"
        
        if not category:
            errors['category'] = "Category is required"
    
        if not description:
            errors['description'] = "Description is required"

        # If there are validation errors, return with errors and the data entered
        if errors:
            return render(request, 'main/notice.html', {
                'errors': errors, 'data': request.POST, 'mode': mode, 'notice': notice
            })

        try:
            if mode == 'create':
                # Create a new notice and automatically set the author to the logged-in user
                notice = Notices.objects.create(
                    title=title,
                    category=category,
                    description=description,
                    author=request.user  # Automatically set the logged-in user as the author
                )
                messages.success(request, "Notice created successfully!")
            else:
                # Edit the existing notice
                notice.title = title
                notice.category = category
                notice.description = description
                notice.save()
                messages.success(request, "Notice updated successfully!")

            return redirect('dashboard')  # Redirect to the dashboard after success
        except Exception as e:
            print(f"Error occurred: {e}")
            messages.error(request, "Failed to save notice.")
            return render(request, 'main/notice.html', {
                'errors': 'Failed to add notice.', 'mode': mode, 'notice': notice
            })

    # For GET requests, fetch all notices for the dashboard
    notices = Notices.objects.all().order_by('-created_at')
    
    return render(request, 'main/notice.html', {
        'mode': mode, 'notice': notice, 'notices': notices
    })


def event_view (request):
    return render(request, 'main/event.html')

def meeting_view (request):
    return render(request, 'main/meeting.html')

def setting_view (request):
    return render(request, 'main/settings.html')