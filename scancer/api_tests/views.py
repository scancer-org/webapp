import requests
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .forms import ImageUploadForm


class PCamImageClassificationView(LoginRequiredMixin, FormView):
    template_name = "api_tests/image_upload.html"
    form_class = ImageUploadForm
    success_url = reverse_lazy("api_tests:pcam-classification")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Test of the Patch Camelyon Image Classification API"
        return context

    def form_valid(self, form):
        r = requests.put(
            "http://localhost:8080/predictions/pcam-classification",
            data=form.cleaned_data["image"],
        )
        number = r.text
        messages.add_message(
            self.request,
            messages.INFO,
            f"The file you uploaded was has this category: {number}",
        )
        return super().form_valid(form)


class CamelyonImageSegmentationView(LoginRequiredMixin, FormView):
    template_name = "api_tests/image_upload.html"
    form_class = ImageUploadForm
    success_url = reverse_lazy("api_tests:camelyon-segmentation")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[
            "title"
        ] = "Test of the Camelyon Image Segmentation API"
        return context

    def form_valid(self, form):
        r = requests.put(
            "http://localhost:8080/predictions/camelyon-segmentation",
            data=form.cleaned_data["image"],
        )
        segments = r.text
        messages.add_message(
            self.request,
            messages.INFO,
            f"The file you uploaded has the following segments {segments}",
        )
        return super().form_valid(form)
