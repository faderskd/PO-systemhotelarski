from django.conf.urls import include, url
from django.contrib import admin

from reservations import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'reservations', views.ReservationViewSet)

rooms_patterns = [
    url(r'^$', views.room_list),
]


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rooms$', include(rooms_patterns, namespace='rooms')),
]
