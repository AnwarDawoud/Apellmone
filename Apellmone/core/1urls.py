from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('salons/', views.salons, name='salons'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('terms_uk/', views.terms_uk, name='terms_uk'),
    # Add language-specific URLs
    path('en/', views.index, name='index_en'),
    path('en/services/', views.services, name='services_en'),
    path('en/salons/', views.salons, name='salons_en'),
    path('en/about/', views.about, name='about_en'),
    path('en/contact/', views.contact, name='contact_en'),
    path('en/terms_uk/', views.terms_uk, name='terms_uk_en'),
    path('uk/', views.index, name='index_uk'),
    path('uk/services/', views.services, name='services_uk'),
    path('uk/salons/', views.salons, name='salons_uk'),
    path('uk/about/', views.about, name='about_uk'),
    path('uk/contact/', views.contact, name='contact_uk'),
    path('uk/terms_uk/', views.terms_uk, name='terms_uk_uk'),
    # Add more language prefixes if needed
    path('change-language/', views.change_language, name='change_language'),
]