from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("api/services/", views.service_list, name="service-list"),
    path("api/vendors/", views.vendor_list, name="vendor-list"),
path("api/services/<int:service_id>/", views.service_detail, name="service-detail"),
]