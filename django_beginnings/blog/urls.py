from django.conf.urls import url

from .views import BlogList, BlogDetail

urlpatterns = [
    url(r'^$', BlogList.as_view()),
    url(r'^posts/(?P<pk>[0-9]+)/$', BlogDetail.as_view()),
]