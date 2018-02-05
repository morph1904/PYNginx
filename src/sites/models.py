from django.db import models
from django.urls import reverse


# Create your models here.
class Sites(models.Model):
    domain = models.CharField(max_length=255, null=False, unique=True)
    ssl = models.BooleanField(default=False, null=False)
    reverse_proxy = models.BooleanField(default=False, null=False)
    proxy_destination = models.CharField(max_length=255, null=True)

    def get_absolute_url(self):
        return reverse('domain', kwargs={'pk': self.pk})
