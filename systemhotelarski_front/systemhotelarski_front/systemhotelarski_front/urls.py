from django.conf.urls import url, include
from django.contrib import admin

from users.views import Register

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/', Register.as_view(), name='register'),
    url('^', include('django.contrib.auth.urls')),
]
