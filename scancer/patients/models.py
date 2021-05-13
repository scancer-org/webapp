from dateutil.relativedelta import relativedelta
from django.db import models
from django.urls import reverse
from django.utils import timezone

from .choices import RISK_CHOICES, SEX_CHOICES


class Patient(models.Model):

    hospital_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=5, choices=SEX_CHOICES, blank=True)
    name = models.CharField(max_length=255, blank=True)
    doctor = models.CharField(max_length=255, blank=True)
    note = models.TextField(blank=True)
    risk = models.IntegerField(choices=RISK_CHOICES, null=True, blank=True)

    class Meta:
        ordering = ["-risk"]

    def __str__(self):
        return f"{self.name} ({self.age.years}{self.sex})"

    def get_absolute_url(self):
        return reverse("patients:detail", args=[str(self.id)])

    @property
    def age(self):
        "Calculate the age of a patient from their date of birth"
        now = timezone.now().date()
        age = relativedelta(now, self.date_of_birth)
        return age

    @property
    def risk_colour(self):
        "Get a Bootstrap colour name associated with the examination risk"
        colour_map = {30: "danger", 20: "warning", 10: "success"}
        return colour_map.get(self.risk, "light")

    @property
    def last_examination(self):
        "Return the last examination for a patient"
        return self.examination_set.last()
