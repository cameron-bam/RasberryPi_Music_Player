
import gdata.youtube
import gdata.youtube.service


class RasberryPiYoutubePlayer():

	def __init__(self, search_terms):
		self.search_terms = search_terms
		self.song = self.get_song(self.search_terms)
		self.start_video()


	def start_video(self):
		'''Start Youtube video'''
	


	def pause_video(self):
		'''Stop the current youtube video'''
		
		
	
	def stop_video(self, browser):
		'''Stop(close) youtube player'''
		#add code here
		 
	
	def play_video(self):
		'''Play the current youtube video'''
		
		
	def get_song(self, search_terms):
		'''Initializes the youtube service and plays a song '''	

		yt_service = gdata.youtube.service.YouTubeService()
	
		# Turn on HTTPS/SSL access.
		yt_service.ssl = True
		#Developer Key
		yt_service.developer_key = 'AI39si71VwXnUB0txaRgzJBqVClvLxWbnAf7f_Q_NUnwKsq_QbaZz3UmiGMwW95fTQWnT9OR_T7CpwXk-Dr3w12QdSvlhyFatw'
		#Query 
		query = gdata.youtube.service.YouTubeVideoQuery()
 	 	query.vq = search_terms
  		query.orderby = 'viewCount'
  		feed = yt_service.YouTubeQuery(query)
		entry = feed.entry[0]
		song_url =  entry.media.player.url
		song_id = song_url.split("v=")[1][:11]
		print song_id
		return song_id
	
	

	
