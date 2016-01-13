import requests
import json
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
    #localhost:8001/reservations
    #przelatywac po wszystkich, zbierac nieaktywne i wypisywac, zwracac jako reservation
    #enddate<currentdate
    
class ReservationHistoryList(LoginRequiredMixin, ListView):
    template_name = 'reservations/reservation_history_list.html'

    def get_queryset(self):
        """
        w tej metodzie trzeba zassac rezerwacje usera z api i zwrocic.
        """
        r = requests.get('http://localhost:8001/reservations')
        r = r.json()
        reservations = []
        for x in r :

            enddate = x["end_date"]
            enddate = datetime.datetime.strptime(enddate, "%Y-%m-%d")
            currentdate = datetime.datetime.now()
            if currentdate + datetime.timedelta(days=600) < enddate:
                continue
            if not x["is_active"]:
                reservations.append(x)
             
        
        
        
        
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
