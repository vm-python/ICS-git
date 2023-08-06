from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Company


# Create your views here.

def home(request):
    context = {
        'companies': Company.objects.all()
    }
    return render(request, 'dashboard/home.html', context)


@login_required
def about(request):
    return render(request, 'dashboard/about.html')
