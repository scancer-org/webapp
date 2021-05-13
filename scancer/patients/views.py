from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Patient


class PatientListView(LoginRequiredMixin, ListView):

    model = Patient
    context_object_name = "patients"
    template_name = "patients/list.html"

    def get_queryset(self):
        risk = self.request.GET.get("risk")
        if risk:
            return Patient.objects.filter(risk=risk)
        else:
            return Patient.objects.all()


class PatientDetailView(LoginRequiredMixin, DetailView):

    model = Patient
    context_object_name = "patient"
    template_name = "patients/detail.html"
