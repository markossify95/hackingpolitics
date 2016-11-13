from django.conf.urls import url, include
from .views import *

# /parliament/
urlpatterns = [
    url(r'^member/(?P<pk>[0-9]+)$', MemberInstance.as_view(), name='member'),
    url(r'^member/(?P<fk>[0-9]+)/acts/$', MemberActsView.as_view(), name='member-acts-view'),
    # url(r'^$', views.index, name=''),
]
