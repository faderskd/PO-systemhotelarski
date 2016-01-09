from django.views.generic import ListView

from braces.views import LoginRequiredMixin


class ReservationList(LoginRequiredMixin, ListView):
    template_name = 'reservations/reservation_list.html'
    queryset = []