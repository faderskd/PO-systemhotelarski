import requests
from django.views.generic import ListView
from django.shortcuts import redirect

from braces.views import LoginRequiredMixin


class ReservationList(LoginRequiredMixin, ListView):
    template_name = 'reservations/reservation_list.html'

    def get_queryset(self):
        """
        w tej metodzie trzeba zassac rezerwacje usera z api i zwrocic.
        """
        user = self.request.user
        user_pk = user.pk
        r = requests.get('http://localhost:8001/reservations/')
        reservations = r.json()
        return reservations


def index(request):
    if request.user.is_authenticated():
        return redirect('reservation_list')
    else:
        return redirect('login')