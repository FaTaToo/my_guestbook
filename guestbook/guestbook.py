import cgi
import webapp2

MAIN_PAGE_HTML = """\
<html>
	<body>
		<form action="/sign" method="post">
			<div><textarea name="content" rows="3" cols="60"></textarea></div>
			<div><input type="submit" value="Sign Guestbook"></input></div>
		</form>
	</body>
</html>
"""


class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.write(MAIN_PAGE_HTML)


class Guestbook(webapp2.RequestHandler):
	def post(self):
		self.response.write('<html><body>You wrote: <pre>')
		# t uses cgi.escape() to escape HTML special characters to their character entity equivalents.
		self.response.write(cgi.escape(self.request.get('content')))
		self.response.write('</pre></body></html>')


app = webapp2.WSGIApplication([
	('/', MainPage),
	('/sign', Guestbook)
], debug=True)

# https://cloud.google.com/appengine/docs/python/gettingstartedpython27/handlingforms