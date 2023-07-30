from django.http import HttpResponse
from django.shortcuts import render
from .models import Company


# Create your views here.

def home(request):
    context = {
        'companies': Company.objects.all()
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')
