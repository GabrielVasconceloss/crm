from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import StatusForm, CustomerForm, OpportunityForm
from .models import Camp, Status, Customer, Opportunity
from django.urls import reverse_lazy


@login_required
def flow(request):
    status = Status.objects.all()
    opportunities_list = Opportunity.objects.all()
    return render(request, 'flow.html', {'status_list': status, 'opportunities_list': opportunities_list})


@login_required
def creatCamp(request):
    return render(request, 'addcamp.html')


@login_required
def add_status(request):
    btn_description = 'Add Status'
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('opportunity_kanban')
    else:
        form = StatusForm()
    return render(request, 'add_status.html', {'form': form, 'btn_description': btn_description})


@login_required
def edit_status(request, status_id):
    status = get_object_or_404(Status, id=status_id)
    btn_description = 'Edit Status'
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('opportunity_kanban')
    else:
        form = StatusForm(instance=status)

    return render(request, 'add_status.html', {'form': form, 'status': status, 'btn_description': btn_description})


@login_required
def delete_status(request, status_id):
    status = get_object_or_404(Status, id=status_id)
    status.delete()
    return redirect('opportunity_kanban')


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

@login_required
def opportunity_list(request):
    opportunities = Opportunity.objects.all()
    return render(request, 'opportunity_list.html', {'opportunities': opportunities})

@login_required
def add_opportunity(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    #btn_description = 'Edit Opportunity'
    btn_description = 'Add Opportunity'
    if request.method == 'POST':
        form = OpportunityForm(request.POST)
        if form.is_valid():
            opportunity = form.save(commit=False)
            opportunity.customer = customer
            opportunity.save()
            return redirect('customer_list')
    else:
        form = OpportunityForm()

    return render(request, 'add_opportunity.html', {'form': form, 'customer': customer, 'btn_description': btn_description})

@login_required
def opportunity_kanban(request):
    status_list = Status.objects.all()
    opportunities_list = Opportunity.objects.all()
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('opportunity_kanban')
    else:
        form = StatusForm()
    return render(request, 'opportunity_kanban.html', {'status_list': status_list, 'opportunities_list': opportunities_list, 'form': form})

@login_required
def opportunity(request, opportunity_id):
    opportunity = get_object_or_404(Opportunity, id=opportunity_id)
    return render(request, 'opportunity.html', {'opportunity': opportunity})