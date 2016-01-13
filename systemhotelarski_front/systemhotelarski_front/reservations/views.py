import requests
import json
from django.views.generic import ListView, FormView
from django.shortcuts import redirect

from braces.views import LoginRequiredMixin

from .forms import ReservationForm


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
    
    def form_valid(self, form):
        data = form.cleaned_data
        start_date = data['start_date'].strftime('%Y-%m-%d')
        end_date = data['end_date'].strftime('%Y-%m-%d')
        capacity = str(data['capacity'])
        user = str(self.request.user.pk)
        print(user)
        send_data = json.dumps({'start_date':start_date, 'end_date':end_date, 'capacity':capacity, 'user_pk':user})
        print(send_data)
        r = requests.post('http://localhost:8001/reservations/',data=send_data)
        return super(AddReservation,self).form_valid(form)
