import playVideo
import webapp2
import jinja2
import cgi
import os
import urllib
import speechToText


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

class YoutubePlayer(webapp2.RequestHandler):
	
    def get(self):
	speechEngine = speechToText.SpeechToText('test.flac')
	response = speechEngine.response[0]
	confidence = speechEngine.response[1]
	player = playVideo.RasberryPiYoutubePlayer(response)
	videoID = player.song
        template_values = {
            'videoID' : videoID,
        }
	
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

application = webapp2.WSGIApplication([
	('/', YoutubePlayer),
	('/sign', ),
], debug=True)

