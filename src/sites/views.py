from __future__ import unicode_literals
from django.views.generic import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from braces.views import FormMessagesMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .nginx import nginx as nginx_helper

from . import models
from .forms import SiteForm


# Create your views here.
class SiteIndex(LoginRequiredMixin, ListView):
    template_name = "sites/index.html"
    model = models.Sites


class SiteCreate(FormMessagesMixin, LoginRequiredMixin, CreateView):
    template_name = 'sites/forms/CreateSite.html'
    form_class = SiteForm
    form_valid_message = 'Site Created!'
    form_invalid_message = 'Something went wrong. Your site was not created. Please check the form below.'
    success_url = '/sites/'

    def form_valid(self, form):
        self.object = form.save()
        site = self.object
        nginx = nginx_helper.nginx_create(site)
        response = super(SiteCreate, self).form_valid(form)
        return response


class SiteUpdate(FormMessagesMixin, LoginRequiredMixin, UpdateView):
    model = models.Sites
    fields = ['proxy_destination', 'reverse_proxy']
    template_name = 'sites/forms/UpdateSite.html'
    form_valid_message = 'Site Updated!'
    form_invalid_message = 'Something went wrong. Please check the form below.'
    success_url = '/sites/'


class SiteDelete(FormMessagesMixin, LoginRequiredMixin, DeleteView):
    template_name = 'sites/forms/DeleteSite.html'
    model = models.Sites
    form_valid_message = 'Site Deleted!'
    form_invalid_message = 'Your site was not created. Please check the form below.'
    success_url = '/sites/'



