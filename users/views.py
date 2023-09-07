from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from django.views.generic import (
    UpdateView
)

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
        else:
            messages.error(request, f'Error!')
            return render(request, 'users/register.html', {'form': form})

    else:
        form = UserRegistrationForm()
        return render(request, 'users/register.html', {'form': form})
    

@login_required
def profile(request):
    return render(request, 'users/profile.html')


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ["image"]