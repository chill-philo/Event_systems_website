from django.shortcuts import render
from .models import Service
def home(request):
    services  =Service.objects.all()
    services_1 = services[0]
    name = "Musiime Philip"
    age = 18
    context={"service":services_1,"services":services}
    return render(request,"home.html",context)

