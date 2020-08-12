from django import forms
from .models import Post, Profile

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','pub_date','profile']
        widgets = {}

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {}

class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['prof_pic','bio']

