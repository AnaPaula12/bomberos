from django.conf.urls import url

from . import views

app_name = 'roperia'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<persona_id>[0-9]+)/$', views.detalle_persona, name='detalle'),
    url(r'/ropa/^(?P<ropadeincendio_id>[0-9]+)/$', views.detalle_ropa, name='detalle_ropa'),

]
