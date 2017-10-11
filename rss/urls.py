#from django.conf.urls import url
from django.conf.urls import *
from django.conf import settings
from rss.feeds import RssFeed, AtomFeed
from rss.views import *
from . import views



feeds = {'rss': RssFeed, 'atom': AtomFeed}

urlpatterns= [
	#Class-based views
	url(r'^$', RssLV.as_view(), name='Rssindex'),
	url(r'^(?P<pk>\d)/$', RssDV.as_view(), name='Rssdetail'),
   # url(r'^/feed/$', 'myweb.rss.views.rssfeed'),
    url(r'^feed/$', views.rssfeed, name='rssfeed' ),
#	url(r'^/feed/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
]