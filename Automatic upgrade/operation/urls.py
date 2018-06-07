from django.conf.urls import url
from .views import ResourceView,ResourceView1,ReturnIsUpdateView

urlpatterns = [

    url(r'get_version/(?P<machine_sn>\d+)$',ResourceView.as_view()),
    url(r'upfile_change/(?P<machine_sn>\d+)$', ResourceView1.as_view()),
    url(r'chance_change/(?P<machine_sn>\d+)$', ReturnIsUpdateView.as_view()),

]