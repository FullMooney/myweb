from django.conf.urls import url
import practice.views
 
urlpatterns = [
    url(r'^practice/data.json$', practice.views.data_json),
    url(r'^practice/$', practice.views.main_page),
    url(r'^$', practice.views.main_page),
    url(r'^data.json$', practice.views.data_json),
]
