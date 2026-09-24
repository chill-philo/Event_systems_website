from django.urls import path

from . import views


urlpatterns = [
    path(
        "",
        views.home,
        name="home"
    ),

    # Services
    path(
        "api/services/",
        views.service_list,
        name="service-list"
    ),

    path(
        "api/services/<int:service_id>/",
        views.service_detail,
        name="service-detail"
    ),

    # Vendors
    path(
        "api/vendors/",
        views.vendor_list,
        name="vendor-list"
    ),

    path(
        "api/vendors/<int:vendor_id>/",
        views.vendor_detail,
        name="vendor-detail"
    ),

    # Events
    path(
        "api/events/",
        views.event_list,
        name="event-list"
    ),

    path(
        "api/events/<int:event_id>/",
        views.event_detail,
        name="event-detail"
    ),

    # Bookings
    path(
        "api/bookings/",
        views.booking_list,
        name="booking-list"
    ),

    path(
        "api/bookings/<int:booking_id>/",
        views.booking_detail,
        name="booking-detail"
    ),
]