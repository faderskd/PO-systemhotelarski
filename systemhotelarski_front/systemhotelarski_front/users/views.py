from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, FormView
from django.core.urlresolvers import reverse_lazy

from braces.views import LoginRequiredMixin

from .forms import RegisterForm, ChangePasswordForm


class Register(SuccessMessageMixin, CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_message = 'Thank you for registration! You can now log in.'
    success_url = reverse_lazy('login')


class ChangePassword(SuccessMessageMixin, LoginRequiredMixin, FormView):
    template_name = 'users/change_password.html'
    form_class = ChangePasswordForm
    success_message = 'Password changed successfully.'

    def get_form_kwargs(self):
        kwargs = super(ChangePassword, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(ChangePassword, self).form_valid(form)