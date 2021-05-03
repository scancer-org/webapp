import requests
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from .forms import ImageUploadForm


class PCamImageClassificationView(LoginRequiredMixin, FormView):
    template_name = "api_tests/image_analyse.html"
    form_class = ImageUploadForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Test of the Patch Camelyon Image Classification API"
        context["sample_images"] = [
            {
                "name": "Class 0: No metastatic tissue",
                "url": "https://scancer.org/static/images/api-tests/pcam-0.png"
            },
            {
                "name": "Class 1: Has metastatic tissue",
                "url": "https://scancer.org/static/images/api-tests/pcam-1.png"
            }
        ]
        context["category"] = self.request.GET.get('category')
        return context

    def form_valid(self, form):
        r = requests.put(
            "http://localhost:8080/predictions/pcam-classification",
            data=form.cleaned_data["image"],
        )
        self.category = r.text
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("api_tests:pcam-classification") + f"?category={self.category}"


class PCamImageClassificationServeInfoView(APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        r = requests.get("http://localhost:8081/models/pcam-classification")
        return Response(r.json())


class CamelyonImageSegmentationView(LoginRequiredMixin, FormView):
    template_name = "api_tests/image_analyse.html"
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
        return super().form_valid(form)
