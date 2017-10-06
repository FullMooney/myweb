from django.shortcuts import render
from django.views.generic import ListView, DetailView,TemplateView #TemplateView add for tag
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from blog.models import Post
from tagging.models import Tag, TaggedItem # add for tag
from tagging.views import TaggedObjectList # add for tag

##----- search
from django.views.generic.edit import FormView # add class type generic view
from blog.forms import PostSearchForm # add Search Form which defined forms.py
from django.db.models import Q # add class Q for search
from django.shortcuts import render # add shortcut function

# Create your views here.

#----TemplateView
class TagTV(TemplateView):
	template_name = 'tagging/tagging_cloud.html'

#----ListView
class PostLV(ListView):
	model=Post
	template_name = 'blog/post_all.html'
	context_object_name = 'posts'
	paginate_by = 2

class PostTOL(TaggedObjectList):
	model = Post
	template_name = 'tagging/tagging_post_list.html'

#----DetailView
class PostDV(DetailView):
	model = Post	

#-----ArchiveView
class PostAV(ArchiveIndexView):
	model = Post
	date_field = 'modify_date'

class PostYAV(YearArchiveView):
    model = Post
    date_field='modify_date'
    make_object_list=True

class PostMAV(MonthArchiveView):
	model = Post
	date_field = 'modify_date'

class PostDAV(DayArchiveView):
	model = Post
	date_field = 'modify_date'

class PostTAV(TodayArchiveView):
	model = Post
	date_field = 'modify_date'


#---- Form View
class SearchFormView(FormView):
	form_class = PostSearchForm
	template_name = 'blog/post_search.html'

	def form_valid(self, form):
		schWord = '%s' % self.request.POST['search_word']
		post_list = Post.objects.filter(Q(title__icontains=schWord) | Q(description__icontains=schWord) | Q(content__icontains=schWord)).distinct()

		context = {}
		context['form'] =  form
		context['search_term'] = schWord
		context['object_list'] = post_list

		return render(self.request, self.template_name, context) # No Reirection