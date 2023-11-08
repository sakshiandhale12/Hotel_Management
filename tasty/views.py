from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import authenticate, login
from .models import Menu, Speciality, RegisterModel, Blog, LoginForm, About
from .forms import ReservationForm
from .forms import LoginForm
from django.urls import reverse


def menu(request):
    menu_items = Menu.objects.all()
    return render(request, 'tasty/menu.html', {'menu_items': menu_items})
    
def home(request):
    return render(request, 'tasty/home.html')

def speciality(request):
    specialities = Speciality.objects.all()
    return render(request, 'tasty/speciality.html', {'specialities': specialities})

def reservations(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Save the reservation to the database
            form.save()
            # Redirect to a thank you page or any other appropriate action
            return redirect('thank_you')  # Adjust the URL name as needed
    else:
        form = ReservationForm()

    return render(request, 'tasty/reservations.html', {'form': form})

def blog(request):
    blog_posts = Blog.objects.all()
    return render(request, 'tasty/blog.html', {'blog_posts': blog_posts})

def thank_you(request):
    return render(request, 'tasty/thank_you.html')

def about(request):
    about_content = About.objects.first()
    return render(request, 'tasty/about.html', {'about_content': about_content})

from django.shortcuts import render, redirect
from .forms import ReservationForm

def contact(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Save the reservation to the database
            form.save()
            # Redirect to a thank you page or any other appropriate action
            return redirect('thank_you')  # Adjust the URL name as needed
    else:
        form = ReservationForm()

    return render(request, 'tasty/contact.html', {'form': form})


class CustomLoginView(View):
    template_name = 'tasty/login.html'
    form_class = LoginForm  # Replace with your actual login form

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse_lazy('login'))  # Redirect to the 'tasks' view upon successful login

        return render(request, self.template_name, {'form': form})

def register(request):
    registered_items = RegisterModel.objects.all()
    return render(request, 'tasty/register.html', {'registered_items': registered_items})
