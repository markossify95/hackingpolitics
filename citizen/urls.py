from django.conf.urls import url, include
from .views import *

# /citizen/
urlpatterns = [
    url(r'^user/(?P<pk>[0-9]+)/$', UserInstance.as_view(), name='user'),
]
