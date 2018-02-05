from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.SiteIndex.as_view(), name='index'),
    url(r'^create/$', views.SiteCreate.as_view(), name='create_site'),
    url(r'^update/(?P<pk>\d+)/$', views.SiteUpdate.as_view(), name='update_site'),
    url(r'^delete/(?P<pk>\d+)/$', views.SiteDelete.as_view(), name='delete_site'),

]
