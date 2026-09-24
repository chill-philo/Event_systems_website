from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Service, VendorProfile
from .serializers import ServiceSerializer, VendorProfileSerializer


def home(request):
    services = Service.objects.all()
    services_1 = services[0] if services.exists() else None
    context = {"service": services_1, "services": services}
    return render(request, "home.html", context)


@api_view(["GET"])
def service_list(request):
    services = Service.objects.all()
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def service_detail(request, service_id):
    try:
        service = Service.objects.get(id=service_id)
    except Service.DoesNotExist:
        return Response({"error": "Service not found"}, status=404)

    serializer = ServiceSerializer(service)
    return Response(serializer.data)


@api_view(["GET"])
def vendor_list(request):
    vendors = VendorProfile.objects.all()
    serializer = VendorProfileSerializer(vendors, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def vendor_detail(request, vendor_id):
    try:
        vendor = VendorProfile.objects.get(id=vendor_id)
    except VendorProfile.DoesNotExist:
        return Response({"error": "Vendor not found"}, status=404)

    serializer = VendorProfileSerializer(vendor)
    return Response(serializer.data)