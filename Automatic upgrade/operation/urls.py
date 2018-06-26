from django.conf.urls import url
from .views import ResourceView,ReturnIsUpdateView,DisplayChangefileView,ChangeMachineToViesionView

urlpatterns = [

    url(r'get_version/(?P<machine_sn>\d+)$',ResourceView.as_view()),
    url(r'display_change/$', DisplayChangefileView.as_view()),
    url(r'chance_change/(?P<machine_sn>\d+)$', ReturnIsUpdateView.as_view()),
    url(r'macchange_version/(?P<machine_sn>\d+)$',ChangeMachineToViesionView.as_view())

]