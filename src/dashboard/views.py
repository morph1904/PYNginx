from __future__ import unicode_literals
from django.views import generic

from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models


# Create your views here.
class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = "dashboard/home.html"
