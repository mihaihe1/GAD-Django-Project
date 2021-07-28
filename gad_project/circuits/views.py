from django.shortcuts import render
from .models import Circuit
# Create your views here.


def show_all_circuits(request):
    circuits = Circuit.objects.all()
    return render(request, "circuits.html", {"circuits": circuits})
