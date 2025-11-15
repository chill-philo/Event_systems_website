from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Client)
admin.site.register(models.Vendor)
admin.site.register(models.Booking)
admin.site.register(models.Service)