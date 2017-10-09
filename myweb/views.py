from django.views.generic.base import TemplateView

# add 3 import for auth
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
#Create your vies here

# ---- TemplateView
class HomeView(TemplateView):
	template_name = 'home.html'

# add for auth
# ---- User Creation
class UserCreateView(CreateView):
	template_name = 'registration/register.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
	template_name = 'registration/register_done.html'