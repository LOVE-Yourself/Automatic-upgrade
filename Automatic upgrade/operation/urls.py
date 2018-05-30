from django.conf.urls import url
from .views import ResourceView

urlpatterns = [

    url(r'login/$',ResourceView.as_view()),

]