import requests
from django.views.generic import ListView, FormView
from django.shortcuts import redirect

from braces.views import LoginRequiredMixin

from .forms import ReservationForm, ActivateReservationForm

import datetime
from django.contrib import messages


class ReservationList(LoginRequiredMixin, ListView):
    template_name = 'reservations/reservation_list.html'

    def get_queryset(self):
        """
        w tej metodzie trzeba zassac rezerwacje usera z api i zwrocic.
        """
        user = self.request.user
        user_pk = user.pk
        r = requests.get('http://localhost:8001/reservations/active/user/{pk}'.format(pk=user_pk))
        reservations = r.json()
        return reservations

class RoomList(LoginRequiredMixin, ListView):
    template_name = 'reservations/room_list.html'

    def get_queryset(self):
        return [{'number': 1, 'capacity': 2}, {'number': 2, 'capacity': 4}] 


def index(request):
    if request.user.is_authenticated():
        return redirect('reservation_list')
    else:
        return redirect('login')


class AddReservation(LoginRequiredMixin, FormView):
    template_name = 'reservations/add_reservation.html'
    form_class = ReservationForm


class ActivateReservationView(LoginRequiredMixin, FormView):
    template_name = 'reservations/activate_reservation_form.html'
    form_class = ActivateReservationForm


def change_reservation_status(request, reservation_id, reservation_status):
    o = requests.get('http://localhost:8001/reservations/')
    o = o.json()
    data = None
    for reservation in o:
        if reservation.get('id') == int(reservation_id):
            data = reservation
            break
    opts = {
        True: False,
        False: True
    }
    datetime.datetime.strptime(data.get('start_date'), '%Y-%m-%d')
    date = (
        datetime.datetime.strptime(data.get('start_date'), '%Y-%m-%d'),
        datetime.datetime.strptime(data.get('end_date'), '%Y-%m-%d')
    )
    if datetime.datetime.now() < date[0] or datetime.datetime.now() > date[1]:
        messages.add_message(request, messages.INFO, 'do not!')
        return redirect('reservation_list')
    data['is_active'] = opts[data.get('is_active')]
    print(data)
    r = requests.put('http://localhost:8001/reservations2/{reservation_id}/'.format(reservation_id=reservation_id), data=data)
    return redirect('reservation_list')