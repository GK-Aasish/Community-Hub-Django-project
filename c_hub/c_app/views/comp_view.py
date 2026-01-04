from django.shortcuts import render,redirect

def create_notice(request):
    return render(request, 'components/create_notice.html')

def edit_notice(request, pk):
    notice = get_object_or_404(Notice, pk=pk)

    if request.method == "POST":
        form = NoticeForm(request.POST, instance=notice)
        if form.is_valid():
            form.save()
            return redirect('notice_list')  # redirect back to notice page
    else:
        form = NoticeForm(instance=notice)

    return render(request, 'edit_notice.html', {'form': form, 'notice': notice})
