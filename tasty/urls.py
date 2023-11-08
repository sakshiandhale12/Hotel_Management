from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('speciality/', views.speciality, name='speciality'),
    path('reservations/', views.reservations, name='reservations'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('login/', CustomLoginView.as_view(), name='login'), 
    path('register/', views.register, name='register'),
]
