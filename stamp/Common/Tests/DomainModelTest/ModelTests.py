
import unittest
from Pin import Pin
from PinNotification import PinNotification
from PinLayout import PinLayout
from PinAction import PinAction



class ModelTests(unittest.TestCase):

	#def __init__(self):
	#		self.name = ''


	def test_PinLayout_Success(self):
 			basePinLayout = PinLayout('tty', 'ttle' , 'subtitle', 'fgcolor', 'bgcolor', 'bdy', 'tico')
			#print vars(basePinLayout)
			self.assertIsNotNone(basePinLayout, msg='rizzle')


	def test_PinNotification_Success(self):
 			notificationPinLayout   = PinLayout('tty', 'ttle' , 'subtitle', 'fgcolor', 'bgcolor', 'bdy', 'tico')
 			notification 	        = PinNotification(notificationPinLayout)
			#print vars(notification.layout)
			self.assertIsNotNone(notification)

	def test_Pin_Success(self):
			basePinLayout 		    = PinLayout('tty', 'ttle' , 'subtitle',  'fgcolor', 'bgcolor', 'bdy', 'tico')
			notificationPinLayout   = PinLayout('tty', 'ttle' , 'subtitle',  'fgcolor', 'bgcolor', 'bdy', 'tico')
			pinAction 				= PinAction('title', 'type', 'launchcode')
			pinActions	            = [pinAction]
 			notification 	        = PinNotification(notificationPinLayout)
			pin 			        = Pin('someid', '01/01/2015', 2, notification, basePinLayout, pinActions)
			#print vars(pin)
			self.assertIsNotNone(pin)




if __name__ == '__main__':
	unittest.main()

#md = ModelTests()
#md.PinLayout_Success()
#md.PinNotification_Success()
#md.Pin_Success()