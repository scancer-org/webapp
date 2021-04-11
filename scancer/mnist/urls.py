from django.urls import path

from .views import (
    ImageClassifierView,
)

app_name = "mnist"
urlpatterns = [
    path("classifier", view=ImageClassifierView.as_view(), name="classifier"),
]
