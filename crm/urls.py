from django.urls import path
from . import views

urlpatterns = [
    path('flow/', views.flow, name='flow'),
    path('addcamp/', views.creatCamp, name='addcamp')
]