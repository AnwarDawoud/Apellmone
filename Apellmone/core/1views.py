from django.shortcuts import render
from django.utils.translation import activate
from django.http import JsonResponse
from django.utils import translation
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
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
    return redirect(reverse('index'))

def set_language(request, language_code):
    activate(language_code)
    
def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def salons(request):
    return render(request, 'salons.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

from django.template import loader

def terms_uk(request):
    return render(request, 'core/terms_uk.html')
