from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Event, Service, VendorProfile
from .serializers import EventSerializer, ServiceSerializer, VendorProfileSerializer

@api_view(["GET"])
def event_list(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def event_detail(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        return Response({"error": "Event not found"}, status=404)

    serializer = EventSerializer(event)
    return Response(serializer.data)
def home(request):
    services = Service.objects.all()
    services_1 = services[0] if services.exists() else None
    context = {"service": services_1, "services": services}
    return render(request, "home.html", context)


@api_view(["GET"])
def service_list(request):
    services = Service.objects.all()

    search = request.GET.get("search")
    category = request.GET.get("category")

    if search:
        services = services.filter(
            name__icontains=search
        ) | services.filter(
            description__icontains=search
        )

    if category:
        services = services.filter(category__id=category)

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