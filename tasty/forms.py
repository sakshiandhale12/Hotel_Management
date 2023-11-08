from django import forms
from .models import Reservations , LoginForm , contact# Import the Reservations model here

class ReservationForm(forms.ModelForm):
    # Define custom widgets for form fields
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Reservations  # Specify the Reservations model here
        # fields = ['name', 'email', 'phone', 'date', 'time']
        fields = '__all__'
from django import forms

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=True, label='Your Message')

    class Meta:
        model = LoginForm  # Replace 'YourModel' with the actual model you're using
        fields = '__all__'

class contact(forms.ModelForm):
    name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model =  contact# Specify the Reservations model here
        # fields = ['name', 'email', 'phone', 'date', 'time']
        fields = ['name', 'email', 'message'] 