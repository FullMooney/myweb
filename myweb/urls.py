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
from django.contrib import admin
#from home import views
from django.conf.urls.static import static  # add for photo
from django.conf import settings  # add for photo
from myweb.views import HomeView, UserCreateView, UserCreateDoneTV # for auth

#from bookmark.views import BookmarkLV, BookmarkDV

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # auth URL 3
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    url(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),

    url(r'^$', HomeView.as_view(), name='home'), 
    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
#    url(r'^$', views.index),
    url(r'^photo/', include('photo.urls', namespace='photo')), # add for photo

    url(r'^rss/', include('rss.urls', namespace='rss')), # add for rss
	# Class-based view for bookmark app
	#url(r'^bookmark/$', BookmarkLV.as_view(), name='index'),
	#url(r'^bookmark/(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail')

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # add for photo
