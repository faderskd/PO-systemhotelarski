from django.conf.urls import include, url
from django.contrib import admin

from reservations import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'reservations2', views.ReservationViewSet)

rooms_patterns = [
    url(r'^$', views.room_list),
]

reservations_patterns = [
    url(r'^$', views.reservation_list),
    url(r'^active$', views.reservation_active_list),
    url(r'^inactive$', views.reservation_inactive_list),
    url(r'^active/user/(?P<user_pk>[0-9]+)$', views.user_reservation_list_active),
    url(r'^inactive/user/(?P<user_pk>[0-9])$', views.user_reservation_list_inactive),
    # url(r'^(?P<pk>[0-9]+)$', views.room_list),
]


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^reservations/', include(reservations_patterns)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rooms/', include(rooms_patterns, namespace='rooms')),
]
