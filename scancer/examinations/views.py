from io import BytesIO

import openslide
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from openslide import open_slide
from openslide.deepzoom import DeepZoomGenerator
from PIL import Image, ImageOps

from .models import Examination, Scan

DEEPZOOM_SLIDE = None
DEEPZOOM_FORMAT = "jpeg"
DEEPZOOM_TILE_SIZE = 96
DEEPZOOM_OVERLAP = 1
DEEPZOOM_LIMIT_BOUNDS = True
DEEPZOOM_TILE_QUALITY = 75
SLIDE_NAME = "slide"


class ExaminationListView(LoginRequiredMixin, ListView):

    model = Examination
    context_object_name = "examinations"
    template_name = "examinations/list.html"


# The following is adapted from a demonstration Flask app in the
# OpenSlide Python repository. Specifically:
# https://github.com/openslide/openslide-python/blob/main/examples/deepzoom/deepzoom_server.py
#
# The original code is released under the terms of the GNU Lesser
# General Public License, version 2.1 and copyright Carnegie Mellon
# University.


class ExaminationDetailView(LoginRequiredMixin, DetailView):

    model = Examination
    context_object_name = "examination"
    template_name = "examinations/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO: Extend the following to allow multiple slides in the
        # future
        scan = self.object.first_scan
        if scan:
            raw_slide = open_slide(scan.file)
            context["slide_url"] = reverse(
                "examinations:detail-slide-dzi", args=[scan.pk]
            )
            try:
                mpp_x = raw_slide.properties[openslide.PROPERTY_NAME_MPP_X]
                mpp_y = raw_slide.properties[openslide.PROPERTY_NAME_MPP_Y]
                context["slide_mpp"] = (float(mpp_x) + float(mpp_y)) / 2
            except (KeyError, ValueError):
                context["slide_mpp"] = 0
        return context


@login_required
def slide_dzi(request, pk):
    scan = get_object_or_404(Scan, pk=pk)
    raw_slide = open_slide(scan.file)
    slide = DeepZoomGenerator(
        raw_slide,
        tile_size=DEEPZOOM_TILE_SIZE,
        overlap=DEEPZOOM_OVERLAP,
        limit_bounds=DEEPZOOM_LIMIT_BOUNDS,
    )
    response = slide.get_dzi(DEEPZOOM_FORMAT)
    return HttpResponse(response, content_type="application/xml")


@login_required
def tile(request, pk, level, col, row):
    scan = get_object_or_404(Scan, pk=pk)
    raw_slide = open_slide(scan.file)
    slide = DeepZoomGenerator(
        raw_slide,
        tile_size=DEEPZOOM_TILE_SIZE,
        overlap=DEEPZOOM_OVERLAP,
        limit_bounds=DEEPZOOM_LIMIT_BOUNDS,
    )
    tile = slide.get_tile(level, (col, row))
    buf = BytesIO()
    tile.save(buf, DEEPZOOM_FORMAT, quality=DEEPZOOM_TILE_QUALITY)
    image = Image.open(buf)
    image2 = ImageOps.grayscale(image)
    r = requests.put(
        "http://localhost:8080/predictions/pcam-classification", data=buf.getvalue()
    )
    if r.text == "1":
        image3 = ImageOps.colorize(image2, (255, 0, 0), (255, 255, 255))
    else:
        image3 = ImageOps.colorize(image2, (0, 255, 0), (255, 255, 255))
    response = HttpResponse(content_type="image/jpeg")
    image3.save(response, "JPEG")
    return response
