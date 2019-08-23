#TODO: Mock only
from django.http import HttpResponse

from django.shortcuts import render
from appointments.models import Appointment
from appointments.forms import AppointmentForm


def index(request):
    return render(request, 'index.html', {'appointments': Appointment.objects.all()})


def appointment_add(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
        else:
            return render(request, 'appointment_add.html', {'form': form})
    else:
        return render(request, 'appointment_add.html')


def appointment_delete(request, id):
    Appointment.objects.get(id=id).delete()
    return index(request)
