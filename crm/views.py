from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import StatusForm
from .models import Camp, status
from django.urls import reverse_lazy


@login_required
def flow(request):
    Status = status.objects.all()
    return render(request, 'flow.html', {'Status': Status})

def creatCamp(request):
    return render(request, 'addcamp.html')

def add_status(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            status = form.save()
            return redirect('flow')
    else:
        form = StatusForm()
    return render(request, 'add_status.html', {'form': form})

def edit_status(request, status_id):
    Status = get_object_or_404(status, id=status_id)

    if request.method == 'POST':
        form = StatusForm(request.POST, instance=Status)
        if form.is_valid():
            form.save()
            return redirect('flow')
    else:
        form = StatusForm(instance=Status)

    return render(request, 'add_status.html', {'form': form, 'status': Status})

def delete_status(request, status_id):
    Status = get_object_or_404(status, id=status_id)
    Status.delete()
    return redirect('flow')