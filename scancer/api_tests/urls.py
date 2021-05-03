from django.urls import path

from .views import PCamImageClassificationView, CamelyonImageSegmentationView

app_name = "api_tests"
urlpatterns = [
    path("pcam-classification/", view=PCamImageClassificationView.as_view(), name="pcam-classification"),
    path("camelyon-segmentation/", view=CamelyonImageSegmentationView.as_view(), name="camelyon-segmentation"),
]
