import httplib
import urllib


class WebRequest:

	def __init__(self,requestType, apiHostName , headers, requestURL, body):
			self.RequestType = requestType
			self.ApiHostName = apiHostName
			self.Headers 	 = headers
			self.RequestURL  = requestURL
			self.Body 	     = body
			self.Reponse     = ''






	def MakeAPIRequest(self):
   			conn 		  = httplib.HTTPSConnection(self.ApiHostName)
			conn.request(self.RequestType, self.RequestURL, self.Body, self.Headers)
			self.Response = conn.getresponse()
			return self.Response


