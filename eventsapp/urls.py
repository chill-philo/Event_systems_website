from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("api/services/", views.service_list, name="service-list"),
]