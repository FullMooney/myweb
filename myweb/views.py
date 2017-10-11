from django.views.generic.base import TemplateView

# add 3 import for auth
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required # add

#Create your vies here

# ---- TemplateView
class HomeView(TemplateView):
<<<<<<< HEAD

	template_name = 'home.html'
=======
	template_name = 'home.html'

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
>>>>>>> 337c692f2366b9baed7adbdf6ce236a560f3a27d
