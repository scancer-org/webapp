from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class PatientListView(LoginRequiredMixin, TemplateView):

    template_name = "patients/list.html"
