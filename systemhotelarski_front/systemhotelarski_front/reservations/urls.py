from django.conf.urls import url

from .views import ReservationList

urlpatterns = [
    url('^$', ReservationList.as_view(), name='reservation_list'),
]
