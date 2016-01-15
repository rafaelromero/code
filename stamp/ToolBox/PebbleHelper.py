import httplib
import json
import urllib
import random
import datetime
import dateutil
import math
from Pin import Pin
from PinAction import PinAction	
from JsonMachine import JsonMachine


def GetPinTime(date) :
	greenwhichtime = datetime.datetime.utcnow();
	timediff = greenwhichtime - date
	hours = math.floor((timediff.total_seconds())/3600)
	greenwhichtime = date + datetime.timedelta(hours=hours)
	return greenwhichtime


def GetPinName(basePinName, appendValue):
	return basePinName + '_' + appendValue


def GetRequestURL(pinName):
	return '/v1/user/pins/' + pinName


def GetAPIHostName():
	return 'timeline-api.getpebble.com'


def GetRequestHeader():
	apikey     = ''
	userkey    = ''
	headers = {
			'Content-type' : 'application/json',
		    'X-User-Token' : userkey, 
		    'X-API-Key'    : apikey
		  	  }
	return headers



def GetPinBody(pin):
	jsonMachine = JsonMachine()
	body        = jsonMachine.EncodeCustomObject(pin)

	return body









