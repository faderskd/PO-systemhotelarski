from django.conf.urls import url

from .views import ReservationList, RoomList, AddReservation
from . import views

urlpatterns = [
    url('^$', ReservationList.as_view(), name='reservation_list'),
    url('^rooms/$', RoomList.as_view(), name='room_list'),
    url('^add/$', AddReservation.as_view(), name='add_reservation'),
    url('^change_reservation_status/(?P<reservation_id>[0-9]+)/(?P<reservation_status>\w+)/$', views.change_reservation_status, name='change_reservation_status'),
    url('^history/$', views.ReservationHistoryList.as_view(), name='reservation_history_list'),
]
