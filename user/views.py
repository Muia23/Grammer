from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import NewPostForm, EditProfileForm
from .models import Post,User, Profile

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    posts = Post.get_posts() 
    current_user = request.user
    profile = Profile.open_profile(current_user)    
    return render(request, 'index.html', {"posts": posts,"current_user": current_user, "profile": profile })

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

#view function to edit user profile
@login_required(login_url='/accounts/login/')
def edit_profile(request):        
    current_user = request.user
    if request.method == 'POST':
        editform = EditProfileForm(request.POST, request.FILES)
        if editform.is_valid():
            profile = editform.save(commit=False)
            profile.user =  current_user
            profile.save()
        return redirect('home')
    else:
        editform = EditProfileForm()
    return render(request, 'create-profile.html', {"editform": editform})

#view your profile
def profile(request, id):
    current_user = request.user
    profile = Profile.open_profile(id)
    feeds = Post.get_feed(id)
    return render(request, 'profile.html', {"profile": profile ,"current_user": current_user, "feeds": feeds}) 

#view other profile
def profilevisit(request, id):
    profile = Profile.open_profile(id)
    feeds = Post.get_feed(id)
    return render(request, 'visit-profile.html', {"profile": profile , "feeds": feeds}) 


#function to edit pprofile picture and bio
#@login_required(login_url='/accounts/login/')
#def editprofile(request, id):        
#    profiles = Profile.open_profile(id)
#    current_user = request.user
#    if request.method == 'POST':        
#        picture = NewProfilePictureForm(request.POST, request.FILES)                
#        if picture.is_valid():
#            profile = picture.save(commit=False)            
#            profile.user = current_user
#            profile.save()                            
#        return redirect('home')        
#
#    elif request.method == 'POST':                
#        bio = NewBioForm(request.POST, request.FILES)        
#        if bio.is_valid():
#            profile = bio.save(commit=False)
#            profile.user = current_user
#            profile.save()
#        return redirect('home')        
#
#    else:
#        picture = NewProfilePictureForm()
#        bio = NewBioForm()
#    return render(request, 'edit-profile.html', {"profiles": profiles, "picture": picture, "bio": bio})