from django.urls import path

from .views import ExaminationDetailView, ExaminationListView, slide_dzi, tile

app_name = "examinations"
urlpatterns = [
    path("", view=ExaminationListView.as_view(), name="list"),
    path("<int:pk>/", view=ExaminationDetailView.as_view(), name="detail"),
    path("slides/<int:pk>.dzi", view=slide_dzi, name="detail-slide-dzi"),
    path(
        "slides/<int:pk>_files/<int:level>/<int:col>_<int:row>.jpeg",
        view=tile,
        name="detail-slide-tile",
    ),
]
