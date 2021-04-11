from django.urls import path

from .views import PatientListView

app_name = "patients"
urlpatterns = [
    path("", view=PatientListView.as_view(), name="list"),
]
