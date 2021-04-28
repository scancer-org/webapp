from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Patient


class PatientListView(LoginRequiredMixin, ListView):

    model = Patient
    context_object_name = "patients"
    template_name = "patients/list.html"
