from django.db import models
from ckeditor.fields import RichTextField

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

