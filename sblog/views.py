from django.shortcuts import render, get_object_or_404
from sblog.models import Blog
from django.views import generic
from django.http import HttpResponse

# Create your views here.
class BlogListView(generic.ListView):
	template_name = 'sblog/bloglist.html'
	context_object_name = 'blogs'

	def get_queryset(self):
		return Blog.objects.all()

class BlogDtailView(generic.DetailView):
	model = Blog   
	template_name = 'sblog/blogshow.html'