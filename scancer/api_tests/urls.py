from django.urls import path

from .views import DeepLabv3ImageSegmenterView, MNISTImageClassifierView

app_name = "api_tests"
urlpatterns = [
    path("mnist/", view=MNISTImageClassifierView.as_view(), name="mnist"),
    path("deeplabv3/", view=DeepLabv3ImageSegmenterView.as_view(), name="deeplabv3"),
]
