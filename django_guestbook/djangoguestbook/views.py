import logging
import urllib

from google.appengine.api import users, memcache

from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from djangoguestbook.models import Greeting
from djangoguestbook.models import guestbook_key


class MainPageView(TemplateView):
	template_name = "guestbook/main_page.html"

	def get_context_data(self, **kwargs):
		context = super(MainPageView, self).get_context_data(**kwargs)

		# get guestbook_name
		guestbook_name = self.request.GET.get('guestbook_name', 'default_guestbook')
		context['guestbook_name'] = guestbook_name

		# get list of Greeting
		greetings = memcache.get('%s:greetings' % guestbook_name)
		if greetings is None:
			greetings = self.get_queryset()
			if not memcache.add('%s:greetings' % guestbook_name, greetings, 3600 * 24 * 30):
				logging.error('Memcache set failed.')

		context['greetings'] = greetings

		# create login/logout url
		if users.get_current_user():
			url = users.create_logout_url(self.request.get_full_path())
			url_linktext = 'Logout'
		else:
			url = users.create_login_url(self.request.get_full_path())
			url_linktext = 'Login'

		context['url'] = url
		context['url_linktext'] = url_linktext

		return context

	def get_queryset(self):
		guestbook_name = self.request.GET.get('guestbook_name', 'default_guestbook')
		key = guestbook_key(guestbook_name)
		greetings_query = Greeting.query(
			ancestor=key).order(-Greeting.date)
		greetings = greetings_query.fetch(10)

		return greetings

	def post(self, request):
		guestbook_name = request.POST.get('guestbook_name')
		key = guestbook_key(guestbook_name)
		greeting = Greeting(parent=key)

		if users.get_current_user():
			greeting.author = users.get_current_user().nickname()

		greeting.content = request.POST.get('content')
		# save object
		greeting.put()

		# clear cache
		# problem??? why we delete memcache???
		memcache.delete('%s:greetings' % guestbook_name)

		return HttpResponseRedirect('/?' + urllib.urlencode({'guestbook_name': guestbook_name}))