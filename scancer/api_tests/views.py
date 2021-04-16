import requests
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .forms import ImageUploadForm


class PCamImageClassifierView(LoginRequiredMixin, FormView):
    template_name = "api_tests/image_upload.html"
    form_class = ImageUploadForm
    success_url = reverse_lazy("api_tests:pcam")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Test of the Patch Camelyon Image Classifier API"
        return context

    def form_valid(self, form):
        r = requests.put(
            "http://localhost:8080/predictions/pcam_cnn", data=form.cleaned_data["image"]
        )
        number = r.text
        messages.add_message(
            self.request,
            messages.INFO,
            f"The file you uploaded was has this category: {number}",
        )
        return super().form_valid(form)


class DeepLabv3ImageSegmenterView(LoginRequiredMixin, FormView):
    template_name = "api_tests/image_upload.html"
    form_class = ImageUploadForm
    success_url = reverse_lazy("api_tests:deeplabv3")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Test of the DeepLabv3 (ResNet 101 backbone) Image Segmenter API"
        return context

    def form_valid(self, form):
        r = requests.put(
            "http://localhost:8080/predictions/deeplabv3_resnet_101", data=form.cleaned_data["image"]
        )
        segments = r.text
        messages.add_message(
            self.request,
            messages.INFO,
            f"The file you uploaded has the following segments {segments}",
        )
        return super().form_valid(form)
