from dateutil.relativedelta import relativedelta
from django.db import models
from django.utils import timezone

from .choices import SEX_CHOICES


class Patient(models.Model):

    hospital_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=5, choices=SEX_CHOICES, blank=True)
    name = models.CharField(max_length=255, blank=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.age.years}{self.sex})"

    @property
    def age(self):
        "Calculate the age of a patient from their date of birth"
        now = timezone.now().date()
        age = relativedelta(now, self.date_of_birth)
        return age
