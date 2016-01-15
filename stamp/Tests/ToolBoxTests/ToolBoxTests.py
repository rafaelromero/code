from Pin import Pin
from PinNotification import PinNotification
from PinLayout import PinLayout
from PinAction import PinAction
import PebbleHelper



class ToolBoxTests:

	def __init__(self):
			self.name = ''


	def PinLayout_Success(self):
 			basePinLayout = PinLayout('tty', 'ttle' , 'fgcolor', 'bgcolor', 'bdy', 'tico')
			print vars(basePinLayout)


	def PinNotification_Success(self):
 			notificationPinLayout   = PinLayout('tty', 'ttle' , 'fgcolor', 'bgcolor', 'bdy', 'tico')
 			notification 	        = PinNotification()
 			notification.layout     = notificationPinLayout
			print vars(notification.Layout)

	def GetPinBody_Success(self):
			basePinLayout 		    = PinLayout('tty', 'base layout!' ,'subt', 'fgcolor', 'bgcolor', 'base pin body', 'tico')
			notificationPinLayout   = PinLayout('tty', 'ttle' ,  'subt2','fgcolor', 'bgcolor', 'bdy', 'tico')
			pinAction 				= PinAction('actiontitle', 'actiontype', 'actionLaunchCode')
			pinAction2 				= PinAction('actiontitle2', 'actiontype2', 'actionLaunchCode2')
			pinActions	            = [pinAction, pinAction2]
 			notification 	        = PinNotification()
 			notification.Layout     = notificationPinLayout
			pin 			        = Pin('rafeePooIDDD', '01/01/2015', 2, notification, basePinLayout, pinActions)
			body = PebbleHelper.GetPinBody(pin)
			print body


	def ConvertActionsToJson_Success(self):
			basePinLayout 		    = PinLayout('tty', 'base layout!' ,'subt', 'fgcolor', 'bgcolor', 'base pin body', 'tico')
			notificationPinLayout   = PinLayout('tty', 'ttle' ,  'subt2','fgcolor', 'bgcolor', 'bdy', 'tico')
			pinAction 				= PinAction('actiontitle', 'actiontype', 'actionLaunchCode')
			pinAction2 				= PinAction('actiontitle2', 'actiontype2', 'actionLaunchCode2')
			pinActions	            = [pinAction, pinAction2]
 			notification 	        = PinNotification()
 			notification.Layout     = notificationPinLayout
			pin 			        = Pin('rafeePooIDDD', '01/01/2015', 2, notification, basePinLayout, pinActions)
			PebbleHelper.ConvertActionsToJson(pin)


tb = ToolBoxTests()
#tb.PinLayout_Success()
#tb.PinNotification_Success()

tb.GetPinBody_Success()
#tb.ConvertActionsToJson_Success()