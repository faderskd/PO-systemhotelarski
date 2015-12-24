from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView

from .forms import RegisterForm


class Register(SuccessMessageMixin, CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_message = 'Thank you for registration! You can now log in.'

