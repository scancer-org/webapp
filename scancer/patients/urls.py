from django.urls import path

from .views import PatientDetailView, PatientListView

app_name = "patients"
urlpatterns = [
    path("", view=PatientListView.as_view(), name="list"),
    path("<int:pk>/", view=PatientDetailView.as_view(), name="detail"),
]
