"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
#from home import views
from django.conf.urls.static import static  # add for photo
from django.conf import settings  # add for photo
from myweb.views import HomeView, HomeMobiView, UserCreateView, UserCreateDoneTV # for auth
import practice.views
#from bookmark.views import BookmarkLV, BookmarkDV

urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     # auth URL 3
#     url(r'^accounts/', include('django.contrib.auth.urls')),
#     url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
#     url(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),

#     url(r'^$', HomeView.as_view(), name='home'), 
#     url(r'^bookmark/', include('bookmark.urls', )),
#     url(r'^blog/', include('blog.urls', )),
# #    url(r'^$', views.index),
#     url(r'^photo/', include('photo.urls', )), # add for photo

#     # url(r'^rss/', include('rss.urls', )), # add for rss
# 	# Class-based view for bookmark app
# 	#url(r'^bookmark/$', BookmarkLV.as_view(), name='index'),
# 	#url(r'^bookmark/(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail')
#     url(r'^ckeditor/', include('ckeditor_uploader.urls')), # ckeditor

#     # mobile
#     url(r'^m/', HomeMobiView.as_view(), name='mobihome'),

#     #practice
#     url(r'^practice/', include('practice.urls', )),

#     url(r'^bit.json$', HomeView.bitsise),    

    url(r'^admin/', admin.site.urls),
    # auth URL 3
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    url(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),

    url(r'^$', HomeView.as_view(), name='home'), 
    path(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
    path(r'^blog/', include('blog.urls', namespace='blog' )),
#    url(r'^$', views.index),
    path(r'^photo/', include('photo.urls', namespace='photo')), # add for photo

    # url(r'^rss/', include('rss.urls', )), # add for rss
    # Class-based view for bookmark app
    #url(r'^bookmark/$', BookmarkLV.as_view(), name='index'),
    #url(r'^bookmark/(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail')
    url(r'^ckeditor/', include('ckeditor_uploader.urls')), # ckeditor

    # mobile
    url(r'^m/', HomeMobiView.as_view(), name='mobihome'),

    #practice
    url(r'^practice/', include('practice.urls', )),

    url(r'^bit.json$', HomeView.bitsise), 
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # add for photo
