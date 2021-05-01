from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Examination


class ExaminationListView(LoginRequiredMixin, ListView):

    model = Examination
    context_object_name = "examinations"
    template_name = "examinations/list.html"


class ExaminationDetailView(LoginRequiredMixin, DetailView):

    model = Examination
    context_object_name = "examination"
    template_name = "examinations/detail.html"
