

from PinLayout 	     import PinLayout
from PinNotification import PinNotification
from PinAction		 import PinAction

class Pin:

	def __init__(self, id_, time, duration, notification, layout, actions):
			self.id 						= id_
			self.time 						= time
			self.duration 	 				= duration
			self.createNotification  	    = notification
			self.layout 	     			= layout
			#self.actions		    		= actions #[]
			





