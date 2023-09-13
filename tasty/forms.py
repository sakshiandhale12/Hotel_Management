from django import forms
from .models import Reservations

class ReservationForm(forms.ModelForm):
    # Define custom widgets for form fields
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Reservations
        fields = ['name', 'email', 'phone', 'date', 'time']

