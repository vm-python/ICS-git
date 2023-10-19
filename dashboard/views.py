from typing import Optional
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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
    

class CompanyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Company
    fields = ["name", "fed_tax_id", "reg_state", "address", "zip_code"]

    def form_valid(self, form):
        form.instance.officer = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        company = self.get_object()
        user = self.request.user

        return company.officer == user


class CompanyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Company
    success_url = "/"

    def test_func(self):
        company = self.get_object()
        user = self.request.user

        return company.officer == user


class ProjectDetailView(DetailView):
    model = Project


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ["name", "parent_company", "description", "manager"]

    
class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = ["name", "parent_company", "description", "manager"]

    def test_func(self):
        project = self.get_object()
        user = self.request.user

        return project.manager == user


class TaskDetailView(DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["name", "description", "project"]

    
class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ["name", "description", "project"]
