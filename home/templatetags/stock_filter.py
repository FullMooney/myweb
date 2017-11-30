from django import template
from yahoo_finance import Share
from pyowm import OWM
import feedparser
import urllib
import xmltodict
from urllib.parse   import quote
from urllib.request import urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

register = template.Library()


@register.filter(name="get_price")
def get_price(value):
#    jongmok = Share('YHOO')
    #jongmok = Share('YHOO')
     return value
#   jongmok = Share('000660.KS')
#   return "%s"%jongmok.get_price()


@register.filter(name="get_weather")
def get_weather(value):
#   return "test"
    print('weather')
    WAETHERAPI_key = '54bfc8086ddec1998083663d49c57c9a'
    owm = OWM(WAETHERAPI_key)
    obs = owm.weather_at_place('Seoul')
    w = obs.get_weather()
    resultVal ='seoul : ' + w.get_status() + ', '+ str(w.get_temperature(unit='celsius')['temp'])
    print('Seoul : ', w.get_status(), w.get_temperature(unit='celsius')['temp'])
    return resultVal



@register.filter(name="get_airdata")
def get_airdata(value):

    url_1 = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName="
    datalocation = urllib.parse.quote_plus("종로구")
    url_2 = "&dataTerm=month&pageNo=1&numOfRows=10&ServiceKey=kvpslAYfknZmVasn9HiQQbE2iKy%2FxU%2BS8tRQWI4YjE%2BygdoLDgYpxEDJHmIU1lS2Mwp7WxIF%2FD2E208WkTecQA%3D%3D&ver=1.3"

    url = url_1 + datalocation + url_2
    # req = urllib2.Request(url)
    req = urllib.request.urlopen(url)
    #print(url)
    data = req.read()

    xmldata = xmltodict.parse(data)
    # xmldata = feedparser.parse(data)
    xmldata = xmldata["response"]["body"]["items"]
    # xmldata = xmldata["body"]
    #print(xmldata)

    context = {}
    context['xmldata'] = xmldata

    airDataList = xmldata['item']
    #print(airDataList)

    resultAirData = airDataList[1]['pm25Value']
    print(resultAirData)

    #print('------- '+resultAirData)

    return resultAirData