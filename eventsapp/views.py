from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Service
from .serializers import ServiceSerializer


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