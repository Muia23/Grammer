from django.db import models

# Create your models here.
class User(models.Model):
    prof_pic = models.ImageField(upload_to = 'profile/')
    username = models.CharField(max_length= 60)
    bio = models.TextField()

    def __str__(self):
        return self.username

class Post(models.Model):    
    image_name = models.CharField(max_length= 60)
    caption = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    upload_image = models.ImageField(upload_to = 'upload/')

    def __str__(self):
        return self.image_name