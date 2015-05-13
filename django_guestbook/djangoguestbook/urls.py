from django.conf.urls import patterns, url
from djangoguestbook.views import MainPageView

urlpatterns = patterns('',
	url(r'^sign/$', MainPageView.as_view(), name='sign_post' ),
	url(r'^$', MainPageView.as_view(), name='mainpage'),
)