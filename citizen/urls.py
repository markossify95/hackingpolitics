from django.conf.urls import url, include
from .views import *

# /citizen/
urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='register'),
    # url(r'^user/(?P<pk>[0-9]+)/profile$', UserInstance.as_view(), name='user-detail'),
    url(r'^user/(?P<pk>[0-9]+)/$', UserInstance.as_view(), name='user'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^problem/new/$', ProblemInstancePost.as_view(), name='problem_post'),
    url(r'^profile/(?P<pk>[0-9]+)/$', ProfileInstance.as_view(), name='profile'),
    url(r'^problem/(?P<pk>[0-9]+)/$', ProblemInstance.as_view(), name='problem-instance'),
    url(r'^problem/filter', ProblemFilter.as_view(), name='problem-filter'),
    url(r'^problem/vote', Voter.as_view(), name='voter'),

]
