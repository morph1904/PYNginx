from __future__ import unicode_literals
from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from . import models


class SiteForm(ModelForm):
    domain = forms.CharField(max_length=80, required=True)
    ssl = forms.BooleanField(widget=forms.CheckboxInput())
    reverse_proxy = forms.BooleanField(widget=forms.CheckboxInput())
    proxy_destination = forms.CharField(max_length=80, required=False)

    class Meta:
        model = models.Sites
        fields = ['domain', 'proxy_destination', 'ssl', 'reverse_proxy']
