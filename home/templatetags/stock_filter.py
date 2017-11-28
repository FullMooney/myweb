from django import template
import json
import requests


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