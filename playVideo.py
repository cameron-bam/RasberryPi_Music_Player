from selenium import webdriver
import webbrowser
import gdata.youtube
import gdata.youtube.service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

class RasberryPiYoutubePlayer():

	def __init__(self, search_terms):
         	self.search_terms = search_terms
         	self.webbrowser = ""
		self.song = self.get_song(self.search_terms)
		self.song_status = False
		self.start_video()


	def start_video(self):
		'''Start Youtube video'''
		self.webbrowser = webdriver.Firefox()
		self.webbrowser.get(self.song)
		


	def pause_video(self):
		'''Stop the current youtube video'''
		
		if (self.song_status != True):
			self.song_status = True
			elem = self.webbrowser.find_element_by_id("player-branded-banner")
			elem.send_keys("seleniumhq" + Keys.SPACE)
	
	def stop_video(self, browser):
		'''Stop(close) youtube player'''
		#add code here
		 
	
	def play_video(self):
		'''Play the current youtube video'''
		if (self.song_status != False):
			self.song_status = False
			self.song_status = True
                        elem = self.webbrowser.find_element_by_id("player")
                        elem.send_keys("seleniumhq" + Keys.ENTER)
		
	def get_song(self, search_terms):
		'''Initializes the youtube service and plays a song '''	

		yt_service = gdata.youtube.service.YouTubeService()
	
		# Turn on HTTPS/SSL access.
		
		yt_service.ssl = True
		yt_service.developer_key = 'AI39si71VwXnUB0txaRgzJBqVClvLxWbnAf7f_Q_NUnwKsq_QbaZz3UmiGMwW95fTQWnT9OR_T7CpwXk-Dr3w12QdSvlhyFatw'
		query = gdata.youtube.service.YouTubeVideoQuery()
 	 	query.vq = search_terms
  		query.orderby = 'viewCount'
  		query.racy = 'include'
  		feed = yt_service.YouTubeQuery(query)
		entry = feed.entry[0]
		song_url = entry.media.player.url
		return song_url
	
	

if __name__ == "__main__":
	player = RasberryPiYoutubePlayer('Welcome To the Jungle')
	time.sleep(5)
	player.pause_video()
