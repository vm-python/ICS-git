from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Company
from django.views.generic import ListView

# Create your views here.

def home(request):
    context = {
        'companies': Company.objects.all()
    }
    return render(request, 'dashboard/home.html', context)


@login_required
def about(request):
    return render(request, 'dashboard/about.html')


class CompanyListView(ListView):
    model = Company
    # app/model_viewtype.html    dashboard/company_list.html in the templates directory
    template_name = "dashboard/home.html"
    context_object_name = "companies"