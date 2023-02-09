from django.shortcuts import render, redirect
from base.models import UserReservation, UserContact


# Create your views here.
def reservations_list(request):
    lst = UserReservation.objects.filter(is_processed=False)
    return render(request, 'reservations_list.html', context={
        'lst': lst,
    })


def contact_help(request):
    list = UserContact.objects.filter(is_processed=False)
    return render(request, 'contact_help.html', context={
        'list': list,
    })


def update_reservation(request, pk):
    UserReservation.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:reservations_list')


def update_contact_help(request, pk):
    UserContact.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:contact_help')
