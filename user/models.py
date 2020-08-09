from django.db import models

# Create your models here.
class User(models.Model):
    prof_pic = models.ImageField(upload_to = 'profile/')
    username = models.CharField(max_length= 60)
    bio = models.TextField()

    def __str__(self):
        return self.username

    def save_user(self):
        self.save()

class Post(models.Model):    
    image_name = models.CharField(max_length= 60)
    caption = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    upload_image = models.ImageField(upload_to = 'upload/')

    def __str__(self):
        return self.image_name

    def save_post(self):
        self.save()

    def delete_post(self, id):
        Post.objects.get(id = id).delete()        

    def change_caption(self, id):
        post = Post.objects.get(id = id).change(caption = 'new_caption')            
        self.save_post()