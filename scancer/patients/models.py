from django.db import models

from .choices import SEX_CHOICES


class Patient(models.Model):

    hospital_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=5, choices=SEX_CHOICES, blank=True)
    name = models.CharField(max_length=255, blank=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.name
