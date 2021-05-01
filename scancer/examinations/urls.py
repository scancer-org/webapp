from django.urls import path

from .views import ExaminationDetailView, ExaminationListView

app_name = "examinations"
urlpatterns = [
    path("", view=ExaminationListView.as_view(), name="list"),
    path("<int:pk>/", view=ExaminationDetailView.as_view(), name="detail"),
]
