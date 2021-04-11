import requests
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView

from .forms import ImageUploadForm


class MNISTImageClassifierView(LoginRequiredMixin, FormView):
    template_name = "api_tests/mnist.html"
    form_class = ImageUploadForm
    success_url = "/api-tests/mnist"

    def form_valid(self, form):
        r = requests.put(
            "http://localhost:8080/predictions/mnist", data=form.cleaned_data["image"]
        )
        number = r.text
        messages.add_message(
            self.request,
            messages.INFO,
            f"The file you uploaded was the number {number}",
        )
        return super().form_valid(form)
