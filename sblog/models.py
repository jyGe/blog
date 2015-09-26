from django.db import models
from ckeditor.fields import RichTextField
import json

# Create your models here.
class Tag(models.Model):
	tag_name = models.CharField(max_length=20, blank=True)
	create_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.tag_name	

class Author(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField(blank=True)
	website = models.URLField(blank=True)

	def __str__(self):
		return self.name

class Blog(models.Model):
	caption = models.CharField(max_length=50)
	author = models.ForeignKey(Author)
	tags = models.ManyToManyField(Tag, blank=True)
	content = RichTextField(config_name='ckeditor')
	publish_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.caption

class Catalogue(models.Model):
	catalogue_name = models.CharField(max_length=20, blank=True)

	def __str__(self):
		return self.catalogue_name

class Article(models.Model):
	caption = models.CharField(max_length=50)
	author = models.ForeignKey(Author)
	catalogue = models.ForeignKey(Catalogue)
	content = models.TextField()
	publish_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.caption

	class Meta:
		ordering = ['-publish_time']

class WordList(models.Model):
	word_list_caption = models.CharField(max_length=50)
	word_list_content = models.TextField()
	catalogue = models.ForeignKey(Catalogue, default=2)
	publish_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.word_list_caption

	@property
	def get_word(self):
		return self.list.all()

class Word(models.Model):
	word = models.CharField(max_length=20)
	word_description = models.TextField()
	add_time = models.DateTimeField(auto_now_add=True)
	word_list = models.ForeignKey(WordList, related_name='list')

	def __str__(self):
		return self.word

