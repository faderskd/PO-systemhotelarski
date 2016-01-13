from django import forms


class ReservationForm(forms.Form):
    start_date = forms.DateField(label='from')
    end_date = forms.DateField(label='to')
    capacity = forms.IntegerField(label='capacity')

    def clean_capacity(self):
        capacity = self.cleaned_data['capacity']
        if capacity <= 0 or not isinstance(capacity, int):
            raise forms.ValidationError('Invalid capacity')
        return capacity