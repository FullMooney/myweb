#from django.shortcuts import render

from django.views.generic import ListView, DetailView
#from django.views.generic.base import TemplateView
from rss.models import *
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render # add shortcut function

import feedparser

# Create your views here.
def rssfeed(request):
	feeds = feedparser.parse('https://pypi.python.org/pypi?%3Aaction=rss')
	context = {}
	context['feeds'] = feeds

	return render(request,'rss/rss_reader.html',context)


#---ListView
class RssLV(ListView):
	model = Rss

#---DetailView
class RssDV(DetailView):
	model = Rss




def rssfeedCreate(request):
		from django.utils import feedgenerator
		fd = feedgenerator.Rss201rev2Feed(
			title=u'my blog rss',
			link=u'/feed/',
			description=u'this is a rss of my blog',
		)

		for entry in Entries.objects.all().order_by('-created')[:5]:
			fd.add_item(
				title=entry.Title,
				link=u'/entry/%d/' % entry.id,
				description=entry.Content,
				pubdate=entry.created,
				categories=(entry.Category.Title,)
			)

		return HttpResponse(fd.writeString('utf-8'), content_type='application/rss+xml')

		#---TemplateView
#class HomeView(TemplateView):
#	teplate_name = 'home.html'