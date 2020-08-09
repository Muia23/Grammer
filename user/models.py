from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Post(models.Model):    
    image_name = models.CharField(max_length= 60)
    caption = HTMLField(blank= True)
    post_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
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

    @classmethod
    def get_posts(cls):
        posts = cls.objects.order_by('-post_date')
        return posts

    #@classmethod
    #def get_feed(cls, id):
    #    posts = cls.objects.filter( user= id)
    #    return posts


#class Customer(models.Model):
#    prof_pic = models.ImageField(upload_to = 'profile/')
#    username = models.CharField(max_length= 60)
#    bio = models.TextField( blank=True)
#
#    def __str__(self):
#        return self.username
#
#    def save_user(self):
#        self.save()
#            
#    @classmethod
#    def open_profile(cls, id):
#        profile = cls.objects.filter(id = id)
#        return profile