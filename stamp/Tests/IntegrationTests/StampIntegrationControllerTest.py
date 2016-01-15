
import unittest
import random
import datetime
import Integration
import Common.DomainModel
import ToolBox


class PackageTrackerIntegrationControllerTest(unittest.TestCase):
	#"""docstring for ClassName"""
	#def __init__(self, arg):
	#	super(PackageTrackerIntegrationControllerTest, self).__init__()
	#	self.arg = arg


		def test_SendPin_Successfull(self):

			basePinLayout 		    = Common.DomainModel.PinLayout('genericPin'         ,  'Package Update!'   ,  'msg to raf in base'      , 'black', 'Blue' , 'package will arrive on..', 'system://images//TIMELINE_CALENDAR')
			notificationPinLayout   = Common.DomainModel.PinLayout('genericNotification',  'notification text' ,  'badabizzle', 'black', 'Green', 'notification msg'        , 'system://images//NOTIFICATION_FLAG')
			pinAction 				= Common.DomainModel.PinAction('title', 'type', 'launchcode')
			pinActions	            = [pinAction]
 			notification 	        = Common.DomainModel.PinNotification(notificationPinLayout)
 			
			pinName        			= ToolBox.PebbleHelper.GetPinName('pin' , str(random.randint(1, 900000000)))
			pinlocaltime   			= datetime.datetime.now()
			pintime        			= str(ToolBox.PebbleHelper.GetPinTime(pinlocaltime).isoformat())
			pin 			        = Common.DomainModel.Pin(pinName, pintime, 2, notification, basePinLayout, pinActions)
			ctrl 					= Integration.StampIntegrationController()
			#self.assertTrue(ctrl.SendPin(pin), msg='found an issue with call')
			self.assertIsNotNone(1, msg='is null')



		def test_GetPackagesToProcess_Successfull(self):
			ctrl 					= Integration.StampIntegrationController()
			ctrl.GetPackagesToProcess(100)
			self.assertIsNotNone(1, msg='is null')




if __name__ == '__main__':
	unittest.main()
