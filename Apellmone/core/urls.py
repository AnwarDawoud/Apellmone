from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('services/', views.services, name='services'),
    path('discounts/', views.discounts, name='discounts'),
    path('location/', views.location, name='location'),
    path('masters/', views.masters, name='masters'),
    path('contact/', views.contact, name='contact'),
    path('terms_uk/', views.terms_uk, name='terms_uk'),
    # Add language-specific URLs
    path('en/', views.home, name='home_en'),
    path('en/aboutus/', views.aboutus, name='aboutus_en'),
    path('en/services/', views.services, name='services_en'),
    path('en/discounts/', views.discounts, name='discounts_en'),
    path('en/location/', views.location, name='location_en'),
    path('en/masters/', views.masters, name='masters_en'),
    path('en/contact/', views.contact, name='contact_en'),
    path('en/terms_uk/', views.terms_uk, name='terms_uk_en'),
    path('uk/', views.home, name='home_uk'),
    path('uk/aboutus/', views.aboutus, name='aboutus_uk'),
    path('uk/services/', views.services, name='services_uk'),
    path('uk/discounts/', views.discounts, name='discounts_uk'),
    path('uk/location/', views.location, name='location_uk'),
    path('uk/masters/', views.masters, name='masters_uk'),
    path('uk/contact/', views.contact, name='contact_uk'),
    path('uk/terms_uk/', views.terms_uk, name='terms_uk_uk'),
    # Add more language prefixes if needed
    path('change-language/', views.change_language, name='change_language'),
]
