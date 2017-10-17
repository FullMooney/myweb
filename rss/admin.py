from django.contrib import admin
from rss.models import Rss

# Register your models here.
# Register your models here.

class RssAdmin(admin.ModelAdmin):
	list_display = ('title','url')

admin.site.register(Rss, RssAdmin)