from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import NewPostForm, NewProfileForm, NewProfilePictureForm, NewBioForm
from .models import Post,User, Profile

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    posts = Post.get_posts()    
    return render(request, 'index.html', {"posts": posts})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
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
        createform = NewProfileForm(request.POST, request.FILES)
        if createform.is_valid():
            profile = createform.save(commit=False)
            profile.user =  current_user
            profile.save()
        return redirect('home')
    else:
        createform = NewProfileForm()
    return render(request, 'create_profile.html', {"createform": createform})


def profile(request, id):
    profiles = Profile.open_profile(id)
    feeds = Post.get_feed(id)
    return render(request, 'profile.html', {"profiles": profiles , "feeds": feeds}) 

#@login_required(login_url='/accounts/login/')
#def editprofile(request, id):        
#    profiles = Profile.open_profile(id)
#    current_user = request.user
#    if request.method == 'POST':        
#        picture = NewProfilePictureForm(request.POST, request.FILES)                
#        if picture.is_valid():
#            profile = picture.save()            
#            profile.user = current_user
#            profile.save()                            
#        return redirect('home')        
#
#    elif request.method == 'POST':                
#        bio = NewBioForm(request.POST, request.FILES)        
#        if bio.is_valid():
#            profile = bio.save()
#            profile.user = current_user
#            profile.save()
#        return redirect('home')    
#
#    else:
#        picture = NewProfilePictureForm()
#        bio = NewBioForm()
#    return render(request, 'edit-profile.html', {"profiles": profiles, "picture": picture, "bio": bio})
