from django.shortcuts import render, get_object_or_404, render_to_response
from sblog.models import Blog, Author
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from sblog.forms import BlogForm
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext

# Create your views here.
class BlogListView(generic.ListView):
	template_name = 'sblog/bloglist.html'
	context_object_name = 'blogs'

	def get_queryset(self):
		return Blog.objects.all()

class BlogDtailView(generic.DetailView):
	model = Blog   
	template_name = 'sblog/blogshow.html'

def to_blog_add(request):
	return render(request, 'sblog/blogadd.html')

def add_blog(request):
	# c = {}
	# c.update(csrf(request))
	if request.method == 'POST':
		form = BlogForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			title = cd['caption']
			author = Author.objects.get(id=1)
			content = cd['content']
			blog = Blog(caption=title, author=author, content=content)
			blog.save()
			id = str(Blog.objects.order_by('-publish_time')[0].id)
			return HttpResponseRedirect(reverse('sblog:detailblog', args=(id,)))
	else:
		form = BlogForm()

	return render_to_response('sblog/blogadd.html', {'form': form}, context_instance=RequestContext(request))

def delete_blog(request, blog_id):
	blog = get_object_or_404(Blog, pk=blog_id)
	if blog:
		blog.delete()
		return HttpResponseRedirect('/sblog/')
	blogs = Blog.objects.all()
	return render_to_response('bloglist.html', {'blogs': blogs})