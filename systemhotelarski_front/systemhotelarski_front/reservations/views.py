from django.views.generic import ListView
from django.shortcuts import redirect

from braces.views import LoginRequiredMixin


class ReservationList(LoginRequiredMixin, ListView):
    template_name = 'reservations/reservation_list.html'
    queryset = []

    def get_queryset(self):
        pass


def index(request):
    if request.user.is_authenticated():
        return redirect('reservation_list')
    else:
        return redirect('login')