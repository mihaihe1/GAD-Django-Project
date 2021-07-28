from django.shortcuts import render, redirect, reverse, Http404
from django.contrib import messages
from .models import Driver
from .forms import AddDriverForm

# Create your views here.


def show_all_drivers(request):
    drivers = Driver.objects.all()
    return render(request, "drivers.html", {"drivers": drivers})


def add_driver(request):
    if request.method == 'GET':
        form = AddDriverForm()

        return render(request, 'add_driver.html', {
            'form': form,
        })

    if request.method == 'POST':
        form = AddDriverForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            messages.success(request, f'Driver was successfully added!')

            return redirect(reverse('drivers:view_all'))

        # form is not valid!
        return render(request, 'add_driver.html', {
            'form': form
        })

    raise Http404('Method not allowed!')