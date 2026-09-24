from django.contrib import admin

from .models import (
    Booking,
    Client,
    Event,
    EventType,
    Service,
    ServiceCategory,
    Vendor,
    VendorProfile,
)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "contacts",
    )


@admin.register(VendorProfile)
class VendorProfileAdmin(admin.ModelAdmin):
    list_display = (
        "company_name",
        "phone",
        "location",
    )


@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
    )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "event_type",
        "event_date",
        "location",
    )
    list_filter = (
        "event_type",
        "event_date",
    )
    search_fields = (
        "name",
        "location",
    )


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
    )


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = (
        "company_name",
        "name",
        "email",
        "phone",
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "vendor_profile",
        "category",
        "price",
    )
    list_filter = (
        "category",
    )
    search_fields = (
        "name",
        "description",
    )


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "client",
        "service",
        "event",
        "event_date",
        "status",
        "created_at",
    )
    list_filter = (
        "status",
        "event_date",
    )
    search_fields = (
        "client__first_name",
        "client__last_name",
        "service__name",
    )