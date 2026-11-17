from django.shortcuts import render, redirect
from .models import SiteSettings
from .forms import ContactRequestModelForm
from .models import SiteSettings, Service


def home(request):
    settings = SiteSettings.objects.first()

    if request.method == 'POST':
        form = ContactRequestModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactRequestModelForm()

    context = {
        "title": "Name_Site",
        "form": form,
        "settings": settings,
    }

    return render(request, template_name='services/home.html', context=context)


def privacy_policy(request):
    settings = SiteSettings.objects.first()

    context = {
        "settings": settings,
    }

    return render(request, 'services/privacy_policy.html', context=context)