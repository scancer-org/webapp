from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Examination


class ExaminationListView(LoginRequiredMixin, ListView):

    model = Examination
    context_object_name = "examinations"
    template_name = "examinations/list.html"
