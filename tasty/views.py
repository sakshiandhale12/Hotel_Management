from django.shortcuts import render
from .models import Menu, Speciality, Reservations, Blog, contact, About


def menu(request):
    menu_items = Menu.objects.all()
    return render(request, 'tasty/menu.html', {'menu_items': menu_items})

def home(request):
    return render(request, 'tasty/home.html')

def speciality(request):
    specialities = Speciality.objects.all()
    return render(request, 'tasty/speciality.html', {'specialities': specialities})

# def reservations(request):
#     if request.method == 'POST':
#         # Handle reservation form submission
#         pass
#     return render(request, 'tasty/reservations.html')


from django.shortcuts import render, redirect
from .forms import ReservationForm

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

def contact(request):
    if request.method == 'POST':
        # Handle contact form submission
        pass
    return render(request, 'tasty/contact.html')
