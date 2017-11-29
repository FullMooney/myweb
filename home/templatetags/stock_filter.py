from django import template
from yahoo_finance import Share
from pyowm import OWM

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



