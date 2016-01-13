from django.conf.urls import url

from .views import ReservationList, RoomList

urlpatterns = [
    url('^$', ReservationList.as_view(), name='reservation_list'),
    url('^rooms/$', RoomList.as_view(), name='room_list'),
]
