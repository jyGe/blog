from django.shortcuts import (render, 
	get_object_or_404,render_to_response, redirect)
from sblog.models import Blog, Author, Tag, Catalogue, Article, Word, WordList
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from sblog.forms import BlogForm, TagForm, LoginForm
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def listing(request):
	blog_list = Blog.objects.order_by('-publish_time')
	paginator = Paginator(blog_list, 5)

	page = request.GET.get('page')
	try:
		blogs = paginator.page(page)
	except PageNotAnInteger:
		blogs = paginator.page(1)
	except EmptyPage:
		blogs = paginator.page(paginator.num_pages)

	return render(request, 'sblog/bloglist.html', {'blogs': blogs})

def blog_tag_list(request, tag_name):
	blogs_list_with_tag = Blog.objects.filter(tags__tag_name=tag_name)

	return render(request, 'sblog/blogtag.html', 
		{'blogs_list_with_tag': blogs_list_with_tag, 
		'tag_name': tag_name})
	# return HttpResponse(blogs_list_with_tag)

class BlogDtailView(generic.DetailView):
	model = Blog   
	template_name = 'sblog/blogshow.html'


def to_blog_add(request):
	return render(request, 'sblog/blogadd.html')

@login_required(login_url='/sblog/login/', redirect_field_name=None)
def add_blog(request):
	if request.method == 'POST':
		form = BlogForm(request.POST)
		tag = TagForm(request.POST)
		if form.is_valid() and tag.is_valid():
			cd_form = form.cleaned_data
			cd_tag = tag.cleaned_data
			tagname = cd_tag['tag_name']
			for taglist in tagname.split():
				Tag.objects.get_or_create(tag_name=taglist.strip())
			title = cd_form['caption']
			author = Author.objects.get(id=1)
			content = cd_form['content']
			blog = Blog(caption=title, author=author, content=content)
			for taglist in tagname.split():
				blog.tags.add(Tag.objects.get(tag_name=taglist.strip()))
				blog.save()
			id = str(Blog.objects.order_by('-publish_time')[0].id)
			return HttpResponseRedirect(reverse('sblog:detailblog', 
												args=(id,)))
	else:
		form = BlogForm()
		tag = TagForm()

	return render_to_response('sblog/blogadd.html',
		{'form': form, 'tag': tag},
		context_instance=RequestContext(request))

@login_required(login_url='/sblog/login/', redirect_field_name=None)
def delete_blog(request, blog_id):
	blog = get_object_or_404(Blog, pk=blog_id)
	if blog:
		blog.delete()
		return HttpResponseRedirect('/sblog/blog/')
	blogs = Blog.objects.all()
	return render_to_response('bloglist.html', {'blogs': blogs})

def user_login(request):
	if request.user.is_authenticated():
		return HttpResponse("在了")
	elif request.POST.get('username'):
		username = request.POST["username"]
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)		
			return redirect('/sblog/blog/')
		else:
			return render_to_response('sblog/login.html',
				{'warning': 'Please check your username and password'}, 
				context_instance=RequestContext(request))
	return render(request, 'sblog/login.html')


def user_logout(request):
	if request.user.is_authenticated():
		logout(request)		
		return listing(request)
	else:		
		return render_to_response('sblog/login.html',
			{'warning': 'Login first'})

def english_catalogue(request):
	catalogues = Catalogue.objects.all()
	articles = Article.objects.all()
	word_lists = WordList.objects.all()
	return render(request, 'sblog/english_catalogue.html',
		{'catalogues': catalogues,
		'articles': articles,
		'word_lists': word_lists,
		})