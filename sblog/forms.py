from django import forms

class BlogForm(forms.Form):
	caption = forms.CharField(max_length=100)
	content = forms.CharField(widget=forms.Textarea)

class TagForm(forms.Form):
	tag_name = forms.CharField()

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField()