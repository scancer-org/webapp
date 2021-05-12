import os

from django.conf import settings
from django.db import models
from django.urls import reverse

from scancer.patients.models import Patient

from .choices import KIND_CHOICES, PRIORITY_CHOICES


def scan_images_path():
    return os.path.join(settings.APPS_DIR, "examples")


def analysis_images_path():
    return os.path.join(settings.APPS_DIR, "examples", "analysis")


class Examination(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField()
    kind = models.CharField(max_length=25, choices=KIND_CHOICES)
    note = models.TextField(blank=True)
    priority = models.CharField(max_length=25, choices=PRIORITY_CHOICES, blank=True)
    healthcare_professional = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.kind} ({self.date})"

    def get_absolute_url(self):
        return reverse("examinations:detail", args=[str(self.id)])

    @property
    def priority_colour(self):
        "Get a Bootstrap colour name associated with the examination priority"
        colour_map = {"high": "danger", "medium": "warning", "low": "success"}
        return colour_map.get(self.priority, "secondary")

    @property
    def first_scan(self):
        "Get the first scan for an examination."
        return self.scan_set.first()


class Scan(models.Model):

    examination = models.ForeignKey(Examination, on_delete=models.CASCADE)
    date = models.DateTimeField()
    file = models.FilePathField(path=scan_images_path)
    heatmap = models.FilePathField(path=analysis_images_path, blank=True, default="")
    # TODO: Incorporate more fields for more analysis data, human
    # annotations and notes

    def __str__(self):
        return f"{self.file} ({self.date})"
