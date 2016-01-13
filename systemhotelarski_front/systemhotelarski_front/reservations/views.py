import requests
from django.views.generic import ListView, FormView
from django.shortcuts import redirect

from braces.views import LoginRequiredMixin

from .forms import ReservationForm, ActivateReservationForm


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
        print("AAA", self.request.user.pk)
        return reservations


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