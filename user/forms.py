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

class EditProfilePicture(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['prof_pic']

class EditBio(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']