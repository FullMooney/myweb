# -*- coding: utf-8 -*-

#from django.shortcuts import render

from django.views.generic import ListView, DetailView
#from django.views.generic.base import TemplateView
from rss.models import *
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render # add shortcut function

import feedparser
import urllib
import xmltodict
from urllib.parse   import quote
from urllib.request import urlopen
from xml.etree.ElementTree import parse

# Create your views here.
def rssfeed(request):
	feeds = feedparser.parse('https://pypi.python.org/pypi?%3Aaction=rss')
	context = {}
	context['feeds'] = feeds
	print(feeds)

	return render(request,'rss/rss_reader.html',context)


def airData(request):

    url_1 = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName="
    datalocation = urllib.parse.quote_plus("종로구")
    url_2 = "&dataTerm=month&pageNo=1&numOfRows=10&ServiceKey=kvpslAYfknZmVasn9HiQQbE2iKy%2FxU%2BS8tRQWI4YjE%2BygdoLDgYpxEDJHmIU1lS2Mwp7WxIF%2FD2E208WkTecQA%3D%3D&ver=1.3"

    url = url_1 + datalocation + url_2
	# req = urllib2.Request(url)
    req = urllib.request.urlopen(url)
    print(url)
    data = req.read()

    xmldata = xmltodict.parse(data)
    #xmldata = feedparser.parse(data)
    xmldata = xmldata["response"]["body"]["items"]
    #xmldata = xmldata["body"]
    print(xmldata)

    context = {}
    context['xmldata'] = xmldata


 #   f = open("./response.txt", "w")

  #  f.write(str(data))
   # f.close()
	# print(data)

    return render(request, 'rss/airdata_reader.html', context)
"""
    tree = parse("response.txt")
    note = tree.getroot()

    strresult = "date  time     :    pm10val:grd      pm2.5val:grd" + "\n"

    for parent in tree.getiterator('item'):
        dataTime = parent.findtext("dataTime")
        so2Value = parent.findtext("so2Value")
        coValue = parent.findtext("coValue")

        o3Value = parent.findtext("o3Value")
        pm10Value = parent.findtext("pm10Value")
        pm10Value24 = parent.findtext("pm10Value24")
        pm25Value = parent.findtext("pm25Value")
        pm25Value24 = parent.findtext("pm25Value24")
        pm10Grade = parent.findtext("pm10Grade")
        pm25Grade = parent.findtext("pm25Grade")

        strresult = strresult + dataTime + "      " + pm10Value + "/" + pm10Grade + "        " + pm25Value + "/" + pm25Grade + "\n"

    return render(request, 'rss/airdata_reader.html', context)

"""


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