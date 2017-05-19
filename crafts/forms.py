from django import forms
from .models import CraftPost, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CraftForm(forms.ModelForm):

	class Meta:
		model = CraftPost
		fields = ('title', 'photo', 'text', 'link', 'postcategory',)

	class Media:
		js = ('/media/tinymce/jscripts/tiny_mce/tiny_mce.js',
                '/sitemedia/js/tinymce_setup.js',)

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ( 'author', 'text',)

	class Media:
		js = ('/media/tinymce/jscripts/tiny_mce/tiny_mce.js',
                '/sitemedia/js/tinymce_setup.js',)
