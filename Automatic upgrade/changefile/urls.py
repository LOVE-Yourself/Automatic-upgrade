from django.conf.urls import url
from .views import ResourceView1

urlpatterns = [

    url(r'upfile_change/(?P<machine_sn>\d+)$', ResourceView1.as_view()),

]