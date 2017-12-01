from django.shortcuts import render, HttpResponse, render_to_response

from django.views.generic import ListView, DetailView
#from django.views.generic.base import TemplateView
from bookmark.models import Bookmark

from django.views.generic.edit import CreateView, UpdateView, DeleteView # for edit
from django.core.urlresolvers import reverse_lazy # for edit
from myweb.views import LoginRequiredMixin # for edit

# chart
import random, json
import pandas as pd
from vincent.colors import brews
from django.db.models import F
import sys

# Create your views here.

#---ListView
class BookmarkLV(ListView):
	model = Bookmark
	def data_json(request):
	    Counts = ['접속자수', ]
	    Costs = ['접속횟수',]
	    # for f in BookmarkLV.model.objects.all():
	    # 	Counts.append(f.title)
	    # 	Costs.append(f.visiters)
	    # data = {
	    #     'columns': [
	    #         Counts,
	    #         Costs,
	    #     ]
	    # }
	    
	    series = []

	    
	    for f in BookmarkLV.model.objects.all():
	    	temp = {}
	    	temp_list =[]
	    	temp['name'] = f.title
	    	temp_list.append(f.visiters)
	    	temp['data'] = temp_list
	    	series.append(temp)

	    
	    print(json.dumps(series))

	    return HttpResponse(json.dumps(series),content_type='text/json')
	def main_page(request):
		return render_to_response('bookmark_list.html')

	

#---DetailView
class BookmarkDV(DetailView):
	model = Bookmark	
	def hit_count(request):
		h_id = request.GET.get("id","")
		mymodel = BookmarkDV.model.objects.filter(id__in=h_id).update(visiters=F('visiters')+1)		
		data = { 'id': [ h_id] }
		return HttpResponse(json.dumps(data),content_type='text/json')
		

# add below for edit 
class BookmarkCreateView(LoginRequiredMixin, CreateView):
	model = Bookmark
	fields = ['title', 'url', 'visiters']
	success_url = reverse_lazy('bookmark:index')

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super(BookmarkCreateView, self).form_valid(form)

class BookmarkChangeLV(LoginRequiredMixin, ListView):
	template_name = 'bookmark/bookmark_change_list.html'

	def get_queryset(self):
		return Bookmark.objects.filter(owner = self.request.user)

class BookmarkUpdateView(LoginRequiredMixin, UpdateView):
	model = Bookmark
	fields = ['title', 'url']
	success_url = reverse_lazy('bookmark:index')

class BookmarkDeleteView(LoginRequiredMixin, DeleteView):
	model = Bookmark
	success_url = reverse_lazy('bookmark:index')

