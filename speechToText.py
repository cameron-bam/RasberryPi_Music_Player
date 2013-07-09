import urllib2

class SpeechToText():

	def __init__(self, file_name):
		'''Initialize the class. The command text and response'''
		self.command = self.enter_command(file_name)
		self.response = self.parse_response(self.command)

	def enter_command(self, file_name):
		'''Using the file name provided, use the google speech api to have it return text from the audio file
		File must be in flac format '''

		url = "https://www.google.com/speech-api/v1/recognize?xjerr=1&client=chromium&lang=en-US"
		audio = open(file_name,'rb').read()
		headers={'Content-Type': 'audio/x-flac; rate=16000', 'User-Agent':'Mozilla/5.0'}
		request = urllib2.Request(url, data=audio, headers=headers)
		response = urllib2.urlopen(request) #Grab response
		return eval(response.read()) #Return the response ( will need to parse after)

	def parse_response(self,response):
		''' Parse the response given back by the google api, returns the text and the confidence level '''
		#Example response: {"status":0,"id":"09cfbeabd8d01ab2d12b1af869c2e42f-1","hypotheses":[{"utterance":"play welcome to the jungle","confidence":0.9095006}]}
	
		resp = response['hypotheses'][0]['utterance']
		confidence = response['hypotheses'][0]['confidence']
		return [resp, confidence]

 
