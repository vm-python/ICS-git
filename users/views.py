from django.shortcuts import render
from .forms import UserRegistrationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        pass
    else:
        form = UserRegistrationForm()
        return render(request, 'users/register.html', {'form': form})