from django.urls import path
from . import views

urlpatterns = [
    path('flow/', views.flow, name='flow'),
    path('addcamp/', views.creatCamp, name='addcamp'),
    path('add_status/', views.add_status, name='add_status'),
    path('/edit_status/<int:status_id>/',views.edit_status, name='edit_status'),
    path('/delete_status/<int:status_id>/', views.delete_status, name='delete_status'),
]