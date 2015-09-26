from django.contrib import admin
from sblog.models import 
	Author, Blog, Tag, Word, WordList, Catalogue, Article

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'website')
	serch_fields = ['name']

class BlogAdmin(admin.ModelAdmin):
	list_display = ('caption', 'id', 'author', 'publish_time')
	list_filter = ['publish_time']
	# date_hierarchy = 'publish_time'
	ordering = ['-publish_time']
	filter_horizontal = ['tags']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)

admin.site.register(Catalogue)
admin.site.register(Article)
admin.site.register(Word)
admin.site.register(WordList)