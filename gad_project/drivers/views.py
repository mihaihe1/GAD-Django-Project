from django.shortcuts import render, redirect, reverse, Http404, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Driver
from .forms import AddDriverForm, FilterDrivers

# Create your views here.


def show_all_drivers(request):
    form = FilterDrivers(request.GET)
    if form.is_valid():
        drivers = form.get_drivers()
        paginator = Paginator(drivers, 3)

        page = request.GET.get('page', 1)
        page_obj = paginator.get_page(page)
        return render(request, "drivers.html", {'page_obj': page_obj, 'form': form})


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


def view_driver(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)
    if request.method == "GET":
        context = {"driver": driver}
        return render(request, "view_driver.html", context)

    if request.method == "POST":
        driver.delete()
        messages.warning(request, f'Driver was successfully deleted!')
        return redirect(reverse('drivers:view_all'))


def update_driver(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)
    form = AddDriverForm(request.POST or None, instance=driver)
    if form.is_valid():
        form.save()

    return render(request, 'add_drivers.html', {'form': form})
