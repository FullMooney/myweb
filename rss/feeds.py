# -*- coding: utf-8 -*-
from rss.models import Entries
#from django.contrib.syndication.feeds import Feed
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed


class RssFeed(Feed):
    title = 'my blog rss'
    link = '/feed/'
    description = 'this is a rss of my blog'

    def item_link(self, item):
        return '/entry/%d/' % item.id

    def item_pubdate(self, item):
        return item.created

    def item_categories(self, item):
        return (item.Category.Title,)

    def items(self):
        return Entries.objects.order_by('-created')[:5]


class AtomFeed(RssFeed):
    feed_type = Atom1Feed
    title_template = 'feeds/rss_title.html'
    description_template = 'feeds/rss_description.html'