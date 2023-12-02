from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .models import Camp
from django.urls import reverse_lazy


@login_required
def flow(request):
    return render(request, 'flow.html')


def creatCamp(request):
    return render(request, 'addcamp.html')

