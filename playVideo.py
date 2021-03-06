
import gdata.youtube
import gdata.youtube.service


class RasberryPiYoutubePlayer():

	def __init__(self, search_terms):
		self.search_terms = search_terms
		self.song = self.play_song(self.search_terms)


		
	def play_song(self, search_terms):
		'''Initializes the youtube service and plays a song '''	

		yt_service = gdata.youtube.service.YouTubeService()
	
		# Turn on HTTPS/SSL access.
		yt_service.ssl = True
		#Developer Key
		yt_service.developer_key = 'AI39si71VwXnUB0txaRgzJBqVClvLxWbnAf7f_Q_NUnwKsq_QbaZz3UmiGMwW95fTQWnT9OR_T7CpwXk-Dr3w12QdSvlhyFatw'
		#Query 
		query = gdata.youtube.service.YouTubeVideoQuery()
 	 	query.vq = search_terms
  		#Order by View count
		query.orderby = 'viewCount'
		#Return feed of videos
  		feed = yt_service.YouTubeQuery(query)
		entry = feed.entry[0]
		song_url =  entry.media.player.url
		#Parse URLto get video id
		song_id = song_url.split("v=")[1][:11]
		return song_id
	
	

	
