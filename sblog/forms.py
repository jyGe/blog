from django import forms

class BlogForm(forms.Form):
	caption = forms.CharField(label='Title', max_length=100)
	content = forms.CharField(widget=forms.Textarea)
