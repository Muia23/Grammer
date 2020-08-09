from .models import Post

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','pub_date']
        widgets = {}