from datetime import datetime

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


# TODO: Save separated in the same form
class Patient(models.Model):
    HONORIFIC_CHOICES = (
        (1, 'Mr'),
        (2, 'Mme'),
    )
    name = models.CharField(max_length=254)
    honorific = models.SmallIntegerField(default=1, choices=HONORIFIC_CHOICES)


class Appointment(models.Model):
    HONORIFIC_CHOICES = (
        (1, 'Mr'),
        (2, 'Mme'),
    )
    day = models.DateField(auto_now=False)
    hour = models.TimeField(auto_now=False)
    duration = models.DurationField(default=15)
    name = models.CharField(max_length=254, blank=True, default='Patient')
    honorific = models.SmallIntegerField(default=1, choices=HONORIFIC_CHOICES)
    # TODO: Separate responsabilities, save and show honorific
    # patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def clean(self):
        if self.day is None or self.day < datetime.now().date():
            raise ValidationError(_('Day cannot be at past'))
