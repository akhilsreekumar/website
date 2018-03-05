from django.conf.urls import url
from sensors import views

urlpatterns = [
    url(r'^sensors/temp/$', views.sensors),
    url(r'^sensors/temp/(?P<pk>[0-9]+)/$', views.sensors_get),
]