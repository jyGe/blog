from django.contrib import admin
from sblog.models import (Author, Blog, Tag,
	Word, WordList, Catalogue, Article)

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

class WordListAdmin(admin.ModelAdmin):
	list_display = ('word_list_caption', 'catalogue','publish_time')
	readonly_fields = ('get_word',)
	fieldsets = (
		(None, {
			'fields': ('word_list_caption', 'catalogue', readonly_fields, 'word_list_content')
		}),
	)


class WordAdmin(admin.ModelAdmin):
	list_display = ('word','word_list','add_time')
	readonly_fields = ('word_list_caption', )
	fieldsets = (
		(None, {
			'fields': ('word', 'word_description','word_list', readonly_fields)
		}),
	)

	def word_list_caption(self, obj):
		return obj.word_list.get_word

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('caption', 'author', 'catalogue', 'publish_time')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)

admin.site.register(Catalogue)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Word, WordAdmin)
admin.site.register(WordList, WordListAdmin)