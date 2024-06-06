from django.shortcuts import render, redirect
from django.utils.translation import activate
from django.http import JsonResponse
from django.utils import translation
from django.urls import reverse
from django.conf import settings

# Define the LANGUAGE_SESSION_KEY manually
LANGUAGE_SESSION_KEY = 'django_language'

def change_language(request):
    if request.method == 'POST':
        user_language = request.POST.get('language')
        if user_language in dict(settings.LANGUAGES):
            translation.activate(user_language)
            request.session[LANGUAGE_SESSION_KEY] = user_language

    # Redirect to the homepage
    return redirect(reverse('home'))

def home(request):
    # Get the list of languages from settings
    languages = settings.LANGUAGES

    # Get the currently selected language code
    language_code = translation.get_language()

    context = {
        'languages': languages,
        'language_code': language_code,
    }

    return render(request, 'home.html', context)

def aboutus(request):
    return render(request, 'aboutus.html')

def services(request):
    return render(request, 'services.html')

def discounts(request):
    return render(request, 'discounts.html')

def location(request):
    return render(request, 'location.html')

def masters(request):
    return render(request, 'masters.html')

def contact(request):
    return render(request, 'contact.html')

def terms_uk(request):
    return render(request, 'terms_uk.html')
