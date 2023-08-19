from django.urls import path
from . import views
from .views import CompanyListView


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("companies/", CompanyListView.as_view(), name="company-list")
]
