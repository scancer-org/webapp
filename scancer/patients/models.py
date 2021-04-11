from django.db import models


class Patient(models.Model):

    dob = models.DateField(max_length=8)
