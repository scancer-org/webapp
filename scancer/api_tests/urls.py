from django.urls import path

from .views import (
    CamelyonImageSegmentationView,
    PCamImageClassificationServeInfoView,
    PCamImageClassificationView,
)

app_name = "api_tests"
urlpatterns = [
    path(
        "pcam-classification/",
        view=PCamImageClassificationView.as_view(),
        name="pcam-classification",
    ),
    path(
        "pcam-classification/serve-info/",
        view=PCamImageClassificationServeInfoView.as_view(),
        name="pcam-classification-serve-info",
    ),
    path(
        "camelyon-segmentation/",
        view=CamelyonImageSegmentationView.as_view(),
        name="camelyon-segmentation",
    ),
]
