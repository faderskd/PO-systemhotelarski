from django.conf.urls import url, include
from django.contrib import admin

from users.views import Register, ChangePassword

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/', Register.as_view(), name='register'),
    url(r'^change-password/', ChangePassword.as_view(), name='change_password'),
    url('^', include('django.contrib.auth.urls')),
]
