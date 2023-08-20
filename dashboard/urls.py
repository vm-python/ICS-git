from django.urls import path
from . import views
from .views import (
    CompanyListView,
    CompanyDetailView,
    CompanyCreateView
)


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("company/", CompanyListView.as_view(), name="company-list"),
    path("company/<int:pk>", CompanyDetailView.as_view(), name="company-detail"),
    path("company/new/", CompanyCreateView.as_view(), name="company-create")
]
