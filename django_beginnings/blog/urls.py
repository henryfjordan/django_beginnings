from django.conf.urls import url

from .views import BlogList, BlogDetail, CommentForm

urlpatterns = [
    url(r'^$', BlogList.as_view(), name='list'),
    url(r'^posts/(?P<pk>[0-9]+)/$', BlogDetail.as_view(), name='detail'),
    url(r'^create/$', CommentForm.as_view(), name='create'),
]