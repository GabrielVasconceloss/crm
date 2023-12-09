from django.urls import path
from . import views

urlpatterns = [
    path('flow/', views.flow, name='flow'),
    path('addcamp/', views.creatCamp, name='addcamp'),
    path('add_status/', views.add_status, name='add_status'),
    path('edit_status/<int:status_id>/',views.edit_status, name='edit_status'),
    path('delete_status/<int:status_id>/', views.delete_status, name='delete_status'),
    path('customer-list/', views.customer_list, name='customer_list'),
    path('add-customer/', views.add_customer, name='add_customer'),
    path('edit-customer/<int:customer_id>/', views.edit_customer, name='edit_customer'),
    path('opportunity-list/', views.opportunity_list, name='opportunity_list'),
    path('add-opportunity/<int:customer_id>/', views.add_opportunity, name='add_opportunity'),
    path('customer-kanban/', views.opportunity_kanban, name='opportunity_kanban'),
]