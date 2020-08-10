from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    url(r'^$', views.index, name='home'),
    url(r'^accounts/profile/', views.index, name='logged_in'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^profile/(\d)/$', views.profile, name='profile'),
    #url(r'^profile/(\d)/edit/$', views.editprofile, name='editprofile'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
