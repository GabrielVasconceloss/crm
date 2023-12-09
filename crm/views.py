from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import StatusForm, CustomerForm
from .models import Camp, status, Customer
from django.urls import reverse_lazy


@login_required
def flow(request):
    Status = status.objects.all()
    return render(request, 'flow.html', {'Status': Status})

@login_required
def creatCamp(request):
    return render(request, 'addcamp.html')

@login_required
def add_status(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            status = form.save()
            return redirect('flow')
    else:
        form = StatusForm()
    return render(request, 'add_status.html', {'form': form})

@login_required
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

@login_required
def delete_status(request, status_id):
    Status = get_object_or_404(status, id=status_id)
    Status.delete()
    return redirect('flow')

@login_required
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})


@login_required
def add_customer(request):
    btn_description = 'Add customer'
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()

    return render(request, 'add_customer.html', {'form': form, 'btn_description': btn_description})

@login_required
def edit_customer(request, customer_id):
    btn_description = 'Edit client'
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer )
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)

    return render(request, 'add_customer.html', {'form': form, 'Customer': customer, 'btn_description': btn_description})
