from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.ReservationList.as_view(), name='reservation_list'),
    url('^activate_reservation_form/$', views.ActivateReservationView.as_view(), name='activate_reservation_form'),
    url('^activate_reservation_form/activate/$', views.ActivateReservationView.as_view(), name='activate_reservation_form'),
]
