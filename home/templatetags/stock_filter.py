from django import template
from yahoo_finance import Share
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

register = template.Library()


@register.filter(name="get_price")
def get_price(value):
<<<<<<< HEAD
#    jongmok = Share('YHOO')
=======
    #jongmok = Share('YHOO')
>>>>>>> 4fb6665ec0cad58ec756806c4958b6fcc2db02fa
    return value
#    jongmok = Share('000660.KS')
#    return "%s"%jongmok.get_price()