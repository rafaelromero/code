import httplib
import json
import urllib
import random
import datetime
import dateutil
import math
import ToolBox
import Common.DomainModel
from   WebRequest 	 import WebRequest


class StampIntegrationController():
	"""docstring for PackageTrackerIntegrationController"""
	def __init__(self):
	#	super(PackageTrackerIntegrationController, self).__init__()
		self.args = 'args'
		

	def SendPin(self, pin):
			pebbleHelper   = ToolBox.PebbleHelper
			pinbody        = pebbleHelper.GetPinBody(pin)
			pinrequesturl  = pebbleHelper.GetRequestURL(pin.id)
			apiHostName    = pebbleHelper.GetAPIHostName()
			headers 	   = pebbleHelper.GetRequestHeader()

			webRequest     = WebRequest('PUT', apiHostName, headers, pinrequesturl, pinbody)
			response       = webRequest.MakeAPIRequest()

			if response.status == 200:
				return True
			else:
				return False











