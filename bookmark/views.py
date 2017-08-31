#from django.shortcuts import render

from django.views.generic import ListView, DetailView
#from django.views.generic.base import TemplateView
from bookmark.models import Bookmark

# Create your views here.

#---ListView
class BookmarkLV(ListView):
	model = Bookmark

#---DetailView
class BookmarkDV(DetailView):
	model = Bookmark

#---TemplateView
#class HomeView(TemplateView):
#	teplate_name = 'home.html'
