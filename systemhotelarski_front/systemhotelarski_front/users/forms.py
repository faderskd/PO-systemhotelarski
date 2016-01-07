import datetime

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label="Password",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control'}))
    password2 = forms.CharField(label="Password confirmation",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control'}),
                                help_text="Enter the same password as above, for verification.")

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'first_name', 'last_name',
                  'date_of_birth')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.TextInput(attrs={'class': 'form-control',
                                                    'placeholder': 'YYYY-MM-DD'}),
        }

    def clean_date_of_birth(self):
        date = self.cleaned_data['date_of_birth']
        current_date = datetime.datetime.now().date()
        if date > current_date:
            raise forms.ValidationError('NOPE')
        return date
