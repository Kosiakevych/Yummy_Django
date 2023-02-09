from django.urls import path
from .views import reservations_list, update_reservation, contact_help, update_contact_help

app_name = 'manager'

urlpatterns = [
    path('reservation/', reservations_list, name='reservations_list'),
    path('reservation/update/<int:pk>/', update_reservation, name='update_reserve'),
    path('contact_help/', contact_help, name='contact_help'),
    path('contact_help/update/<int:pk>/', update_contact_help, name='update_contact_help')
]