from django.urls import path

from .views import ExaminationListView

app_name = "examinations"
urlpatterns = [
    path("", view=ExaminationListView.as_view(), name="list"),
]
