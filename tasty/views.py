from django.shortcuts import render
from .models import Menu, Speciality, Reservations, Blog, contact, About

def home(request):
    return render(request, 'tasty/home.html')


def menu(request):
    menu_items = Menu.objects.all()
    return render(request, 'tasty/menu.html', {'menu_items': menu_items})

def speciality(request):
    specialities = Speciality.objects.all()
    return render(request, 'tasty/speciality.html', {'specialities': specialities})

def reservations(request):
    if request.method == 'POST':
        # Handle reservation form submission
        pass
    return render(request, 'tasty/reservations.html')

def blog(request):
    blog_posts = Blog.objects.all()
    return render(request, 'tasty/blog.html', {'blog_posts': blog_posts})

def about(request):
    about_content = About.objects.first()
    return render(request, 'tasty/about.html', {'about_content': about_content})

def contact(request):
    if request.method == 'POST':
        # Handle contact form submission
        pass
    return render(request, 'tasty/contact.html')
