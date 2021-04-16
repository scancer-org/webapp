from django.urls import path

from .views import PCamImageClassifierView, DeepLabv3ImageSegmenterView

app_name = "api_tests"
urlpatterns = [
    path("pcam/", view=PCamImageClassifierView.as_view(), name="pcam"),
    path("deeplabv3/", view=DeepLabv3ImageSegmenterView.as_view(), name="deeplabv3"),
]
