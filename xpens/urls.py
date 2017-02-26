from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /xpens/
    url(r'^$', views.index, name='index'),
    # ex: /xpens/5/
    url(r'^(?P<xpens_id>[0-9]+)/$', views.detail, name='detail'),
]
