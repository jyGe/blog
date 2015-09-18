from django.conf.urls import url

from . import views

urlpatterns = [
	# url: blog
	url(r'^blog/$', views.listing, name='bloglist'),
	url(r'^blog/(?P<pk>[0-9]+)/$', views.BlogDtailView.as_view(), name='detailblog'),
	url(r'^add/$', views.add_blog, name='addblog'),
	url(r'^blog/(?P<blog_id>[0-9]+)/del/$', views.delete_blog, name='delblog'),
	url(r'^blog/tag/(?P<tag_name>\w+)/$', views.blog_tag_list, name='blogtag'),
	# url(r'^blog/tag/(?P<blog_id>[0-9]+)/$')

	# url: about me
]