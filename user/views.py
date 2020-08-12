from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import NewPostForm, CreateProfileForm, EditProfilePicture, EditBio
from .models import Post,User, Profile,comments

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    posts = Post.get_posts()    
    commenters = comments.get_comments()
    current_user = request.user
    profile = Profile.open_profile(current_user)    

    return render(request, 'index.html', {"posts": posts,"current_user": current_user, "profile": profile, "commenters": commenters })

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
        picture = EditProfilePicture(request.POST, request.FILES)                
        if picture.is_valid():
            profile = picture.save(commit=False)            
            profile.user = current_user
            profile.save()                            
        return redirect('home')        

    if request.method == 'POST':                
        bio = EditBio(request.POST, request.FILES)        
        if bio.is_valid():
            profile = bio.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('home')        

    else:
        picture = EditProfilePicture()
        bio = EditBio()
    return render(request, 'edit-profile.html', {"profiles": profiles, "picture": picture, "bio": bio, "current_user": current_user})