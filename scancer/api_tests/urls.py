from django.urls import path

from .views import MNISTImageClassifierView

app_name = "api_tests"
urlpatterns = [
    path("mnist/", view=MNISTImageClassifierView.as_view(), name="mnist"),
]
