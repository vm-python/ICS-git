from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Company, Project, Task
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)


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
    # <app>/<model>_<viewtype>.html    dashboard/company_list.html in the templates directory
    template_name = "dashboard/home.html"
    context_object_name = "companies"


class CompanyDetailView(DetailView):
    model = Company


class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    fields = ["name", "fed_tax_id", "reg_state", "address", "zip_code"]

    def form_valid(self, form):
        form.instance.officer = self.request.user
        return super().form_valid(form)
    

class CompanyUpdateView(UpdateView):
    model = Company
    fields = ["name", "fed_tax_id", "reg_state", "address", "zip_code"]

    def form_valid(self, form):
        form.instance.officer = self.request.user
        return super().form_valid(form)


class CompanyDeleteView(DeleteView):
    model = Company
    success_url = "/"


class ProjectDetailView(DetailView):
    model = Project


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ["name", "parent_company", "description", "manager"]

    
class ProjectUpdateView(UpdateView):
    model = Project
    fields = ["name", "parent_company", "description", "manager"]


class TaskDetailView(DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["name", "description", "project"]

    
class TaskUpdateView(UpdateView):
    model = Task
    fields = ["name", "description", "project"]
