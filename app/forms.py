from django import forms


class BookingForm(forms.Form):
    first_name = forms.CharField(max_length=100, label='バンド名')
