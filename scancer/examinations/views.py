from io import BytesIO

import openslide
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from openslide import open_slide
from openslide.deepzoom import DeepZoomGenerator

from .models import Examination

DEEPZOOM_SLIDE = None
DEEPZOOM_FORMAT = "jpeg"
DEEPZOOM_TILE_SIZE = 254
DEEPZOOM_OVERLAP = 1
DEEPZOOM_LIMIT_BOUNDS = True
DEEPZOOM_TILE_QUALITY = 75
SLIDE_NAME = "slide"
SLIDE_FILE = str(settings.APPS_DIR / "examples" / "normal_001.tif")


class ExaminationListView(LoginRequiredMixin, ListView):

    model = Examination
    context_object_name = "examinations"
    template_name = "examinations/list.html"


class ExaminationDetailView(LoginRequiredMixin, DetailView):

    model = Examination
    context_object_name = "examination"
    template_name = "examinations/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        raw_slide = open_slide(SLIDE_FILE)
        context["slide_url"] = "/examinations/slide.dzi"
        try:
            mpp_x = raw_slide.properties[openslide.PROPERTY_NAME_MPP_X]
            mpp_y = raw_slide.properties[openslide.PROPERTY_NAME_MPP_Y]
            context["slide_mpp"] = (float(mpp_x) + float(mpp_y)) / 2
        except (KeyError, ValueError):
            context["slide_mpp"] = 0
        return context


def slide_dzi(request):
    raw_slide = open_slide(SLIDE_FILE)
    slide = DeepZoomGenerator(
        raw_slide,
        tile_size=DEEPZOOM_TILE_SIZE,
        overlap=DEEPZOOM_OVERLAP,
        limit_bounds=DEEPZOOM_LIMIT_BOUNDS,
    )
    response = slide.get_dzi(DEEPZOOM_FORMAT)
    return HttpResponse(response, content_type="application/xml")


def tile(request, level, col, row):
    raw_slide = open_slide(SLIDE_FILE)
    slide = DeepZoomGenerator(
        raw_slide,
        tile_size=DEEPZOOM_TILE_SIZE,
        overlap=DEEPZOOM_OVERLAP,
        limit_bounds=DEEPZOOM_LIMIT_BOUNDS,
    )

    tile = slide.get_tile(level, (col, row))
    buf = BytesIO()
    tile.save(buf, DEEPZOOM_FORMAT, quality=DEEPZOOM_TILE_QUALITY)
    return HttpResponse(buf.getvalue(), content_type="image/jpeg")
