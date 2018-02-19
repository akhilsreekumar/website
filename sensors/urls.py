from django.conf.urls import url
from sensors import views

urlpatterns = [
    url(r'^sensors/$', views.sensors),
    url(r'^sensors/(?P<pk>[0-9]+)/$', views.sensors_get),
]