from django.shortcuts import render

from django.views.generic import ListView, DetailView
#from django.views.generic.base import TemplateView
from bookmark.models import Bookmark

from django.views.generic.edit import CreateView, UpdateView, DeleteView # for edit
from django.core.urlresolvers import reverse_lazy # for edit
from myweb.views import LoginRequiredMixin # for edit

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

# add below for edit 
class BookmarkCreateView(LoginRequiredMixin, CreateView):
	model = Bookmark
	fields = ['title', 'url']
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