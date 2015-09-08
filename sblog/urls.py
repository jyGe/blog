from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.BlogListView.as_view(), name='bloglist'),
	url(r'^blog/(?P<pk>[0-9]+)/$', views.BlogDtailView.as_view(), name='detailblog')
]