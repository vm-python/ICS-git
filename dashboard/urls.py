from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("company/", CompanyListView.as_view(), name="company-list"),
    path("company/<int:pk>", CompanyDetailView.as_view(), name="company-detail"),
    path("company/new/", CompanyCreateView.as_view(), name="company-create"),
    path("company/<int:pk>/update/", CompanyUpdateView.as_view(), name="company-update"),
    path("company/<int:pk>/delete/", CompanyDeleteView.as_view(), name="company-delete"),
    path("project/<int:pk>", ProjectDetailView.as_view(), name="project-detail"),
    path("project/new/", ProjectCreateView.as_view(), name="project-create"),
    path("project/<int:pk>/update/", ProjectUpdateView.as_view(), name="project-update"),
    path("task/<int:pk>", TaskDetailView.as_view(), name="task-detail"),
    path("task/new/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update")
]
