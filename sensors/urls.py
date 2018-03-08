from django.conf.urls import url
from sensors import views

urlpatterns = [
    url(r'^sensors/temp/$', views.temper),
    url(r'^sensors/temp/(?P<pk>[0-9]+)/$', views.get_temper),

    url(r'^sensors/press/$', views.press),
    url(r'^sensors/press/(?P<pk>[0-9]+)/$', views.get_press),

    url(r'^sensors/heart/$', views.heart),
    url(r'^sensors/heart/(?P<pk>[0-9]+)/$', views.get_heart),

    url(r'^sensors/glucos/$', views.glucos),
    url(r'^sensors/glucos/(?P<pk>[0-9]+)/$', views.get_glucos),

    url(r'^sensors/all/$',views.all)
]