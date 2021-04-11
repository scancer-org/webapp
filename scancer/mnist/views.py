import requests

from django.views.generic.edit import FormView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ImageUploadForm


class ImageClassifierView(LoginRequiredMixin, FormView):
    template_name = 'mnist/classify.html'
    form_class = ImageUploadForm
    success_url = '/mnist/classifier'

    def form_valid(self, form):
        r = requests.put(
            'http://localhost:8080/predictions/mnist',
            data=form.cleaned_data["image"]
        )
        number = r.text
        messages.add_message(self.request, messages.INFO, f'The file you uploaded was the number {number}')
        return super().form_valid(form)
