from django import forms
from .models import Job_post, Freepost_j

class JPostForm(forms.ModelForm) :
    class Meta:
        model = Job_post
        fields = ['title', 'content', 'image']

class FreePostForm_j(forms.ModelForm):
    class Meta :
        model = Freepost_j
        fields =['title', 'image', 'content']
