from django.views.generic.base import TemplateView

# add 3 import for auth
from blog.models import Post
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required # add
#from django.db.models.loading import get_model


#Create your vies here

# ---- TemplateView
class HomeView(ListView):
	model = Post
	template_name = 'home.html'	
	context_object_name = 'posts'

class HomeMobiView(ListView):
	model = Post
	template_name = 'm/home.html'	
	context_object_name = 'posts'
	paginate_by = 4
	
# add for auth
# ---- User Creation
class UserCreateView(CreateView):
	template_name = 'registration/register.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
	template_name = 'registration/register_done.html'

#-------edit
class LoginRequiredMixin(object):
	@classmethod
	def as_view(cls, **initkwargs):
		view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
		return login_required(view)
