from django import forms
from .models import Comment


class PostShareForm(forms.Form):
    name = forms.CharField(max_length=25)
    to = forms.EmailField()
    email = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
