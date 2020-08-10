from django import forms
from .models import Post, Profile

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','pub_date']
        widgets = {}

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {}





class NewProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['id','bio']
        widgets = {}

class NewBioForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['id','prof_pic']
        widgets = {}