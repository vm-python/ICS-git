from django.shortcuts import render
from .models import Company


# Create your views here.

def home(request):
    context = {
        'companies': Company.objects.all()
    }
    return render(request, 'dashboard/home.html', context)


def about(request):
    return render(request, 'dashboard/about.html')
