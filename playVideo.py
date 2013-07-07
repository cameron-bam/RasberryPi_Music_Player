
import webbrowser
import gdata.youtube
import gdata.youtube.service

def youtube_service(search_terms):
	
	'''Initializes the youtube service and plays a song '''	

	yt_service = gdata.youtube.service.YouTubeService()

	# Turn on HTTPS/SSL access.
	# Note: SSL is not available at this time for uploads.
	yt_service.ssl = True
	yt_service.developer_key = 'AI39si71VwXnUB0txaRgzJBqVClvLxWbnAf7f_Q_NUnwKsq_QbaZz3UmiGMwW95fTQWnT9OR_T7CpwXk-Dr3w12QdSvlhyFatw'
	query = gdata.youtube.service.YouTubeVideoQuery()
  	query.vq = search_terms
  	query.orderby = 'viewCount'
  	query.racy = 'include'
  	feed = yt_service.YouTubeQuery(query)
	entry = feed.entry[0]
	song_url = entry.media.player.url
	play_song(song_url)
	
def play_song(song):
	'''Open a youtube video on firefox browser'''

	webbrowser.get('firefox').open_new_tab(song)

