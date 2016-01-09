from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views

from users.views import Register, ChangePassword

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/', Register.as_view(), name='register'),
    url(r'^change-password/', ChangePassword.as_view(), name='change_password'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout_then_login, name='logout'),
    url('^reservations/', include('reservations.urls')),
]
