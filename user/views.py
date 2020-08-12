from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import NewPostForm, CreateProfileForm, EditProfile
from .models import Post,User, Profile,comments


# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):    
    commenters = comments.get_comments()
    current_user = request.user
    profile = Profile.open_profile(current_user)    
    #thumbs_up = get_object_or_404(Post, id=self.kwargs['post.id'])
    posts = Post.get_posts()   
    #likes = Post.total_likes()
    return render(request, 'index.html', {"posts": posts,"current_user": current_user, "profile": profile, "commenters": commenters}) #, "likes": likes 

def likeview(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return redirect('home')


#create a post
@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.profile = Profile.username
            post.save()
        return redirect('home')
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form":form})

#view function to create user profile
@login_required(login_url='/accounts/login/')
def create_profile(request):        
    current_user = request.user
    if request.method == 'POST':
        createform = CreateProfileForm(request.POST, request.FILES)
        if editform.is_valid():
            profile = createform.save(commit=False)
            profile.user =  current_user
            profile.save()
        return redirect('home')
    else:
        createform = CreateProfileForm()
    return render(request, 'create-profile.html', {"createform": createform})

#view your profile
def profile(request, id):
    current_user = request.user
    profile = Profile.open_profile(id)
    posts = Post.get_posts() 
    feeds = Post.get_feed(id)
    return render(request, 'profile.html', {"profile": profile ,"current_user": current_user, "feeds": feeds, "posts": posts}) 

#view other profile
def profilevisit(request, id):
    profile = Profile.open_profile(id)
    feeds = Post.get_feed(id)
    return render(request, 'visit-profile.html', {"profile": profile , "feeds": feeds}) 

#function to edit user profile and bio
@login_required(login_url='/accounts/login/')
def editprofile(request,id):        
    profiles = Profile.open_profile(id)
    current_user = request.user
    if request.method == 'POST':        
        editprofile = EditProfile(request.POST, request.FILES)                
        if editprofile.is_valid():
            profile = editprofile.save(commit=False)            
            profile.user = current_user
            profile.save()                            
        return HttpResponseRedirect(reverse('editprofile', args=[str(id)]))        

    else:
        editprofile = EditProfile()        
    return render(request, 'edit-profile.html', {"profiles": profiles, "editprofile": editprofile, "current_user": current_user})