from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    contacts = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class VendorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    whatsapp = models.CharField(max_length=20, blank=True)
    instagram = models.URLField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.company_name


class EventType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    event_type = models.ForeignKey(
        EventType,
        on_delete=models.PROTECT,
        related_name="events"
    )
    description = models.TextField(blank=True)
    event_date = models.DateField()
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ServiceCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company_name = models.CharField(max_length=150)

    def __str__(self):
        return self.company_name


class Service(models.Model):
    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE,
        related_name="services"
    )
    vendor_profile = models.ForeignKey(
        VendorProfile,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="services"
    )
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="services"
    )
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ""


class Booking(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("declined", "Declined"),
        ("cancelled", "Cancelled"),
        ("completed", "Completed"),
    ]

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="bookings"
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="bookings",
        null=True,
        blank=True
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="bookings"
    )
    event_date = models.DateField()
    notes = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.client} - {self.service.name}"