from django import template
import json
import requests

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

     rsp = requests.get('https://finance.google.com/finance?q={}&output=json'.format(value))

     if rsp.status_code in (200,):
          # This magic here is to cut out various leading characters from the JSON
          # response, as well as trailing stuff (a terminating ']\n' sequence), and then
          # we decode the escape sequences in the response
          # This then allows you to load the resulting string
          # with the JSON module.
          fin_data = json.loads(rsp.content[6:-2].decode('unicode_escape'))

          # print out some quote data
          print('Opening Price: {}'.format(fin_data['l']))

     return fin_data['l']
#   jongmok = Share('000660.KS')
#   return "%s"%jongmok.get_price()


@register.filter(name="get_weather")
def get_weather(value):
    try:
    #   return "test"
        print('weather')
        WAETHERAPI_key = '54bfc8086ddec1998083663d49c57c9a'
        owm = OWM(WAETHERAPI_key)
        obs = owm.weather_at_place('Seoul')
        w = obs.get_weather()
        resultVal ='seoul, ' + w.get_status() + ', '+ str(w.get_temperature(unit='celsius')['temp'])
        print('Seoul : ', w.get_status(), w.get_temperature(unit='celsius')['temp'])
        return resultVal
    except:
        return 'N/A'


@register.filter(name="get_airdata")
def get_airdata(value):
    try:
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

        #context = {}
        #context['xmldata'] = xmldata

        airDataList = xmldata['item']
        #print(airDataList)

        resultAirData = airDataList[0]['pm25Value']
        print(resultAirData)

        #print('------- '+resultAirData)

        return resultAirData
    except:
        return 'N/A'