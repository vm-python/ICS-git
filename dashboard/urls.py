from django.urls import path
from . import views
from .views import (
    CompanyListView,
    CompanyDetailView,
    CompanyCreateView,
    CompanyUpdateView,
    CompanyDeleteView
)


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("company/", CompanyListView.as_view(), name="company-list"),
    path("company/<int:pk>", CompanyDetailView.as_view(), name="company-detail"),
    path("company/new/", CompanyCreateView.as_view(), name="company-create"),
    path("company/<int:pk>/update/", CompanyUpdateView.as_view(), name="company-update"),
    path("company/<int:pk>/delete/", CompanyDeleteView.as_view(), name="company-delete")
]
