from django.urls import path

from .views import DeepLabv3ImageSegmenterView, PCamImageClassifierView

app_name = "api_tests"
urlpatterns = [
    path("pcam/", view=PCamImageClassifierView.as_view(), name="pcam"),
    path("deeplabv3/", view=DeepLabv3ImageSegmenterView.as_view(), name="deeplabv3"),
]
