import playVideo
import webapp2
import jinja2
import cgi
import os
import urllib
from google.appengine.api import users

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

class Index(webapp2.RequestHandler):
	
    def get(self):

        user = users.get_current_user()
        if user:
		url = users.create_logout_url(self.request.uri)
		url_linktext = 'Logout'
        else:
		url = users.create_login_url(self.request.uri)
            	url_linktext = 'Login'

	template_values = {
		'url': url,
		'url_linktext': url_linktext,
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))



application = webapp2.WSGIApplication([
	('/', Index),
	('/sign', playVideo ),
], debug=True)

