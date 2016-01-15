import os
import unittest
import Config


class ConfigTest(unittest.TestCase):
	#"""docstring for ClassName"""
	#def __init__(self, arg):
	#	super(PackageTrackerIntegrationControllerTest, self).__init__()
	#	self.arg = arg


		def test_BuildConfig_Successfull(self):
			config = Config.Config('Tests/ConfigTest')
			self.assertIsNotNone(config, msg='is null')



		def test_GetValueFromConfig_Successfull(self):
			config = Config.Config('Tests/ConfigTest')
			val = config.Get('mongoserveraddress')
			#self.assertIsNotNone(config, msg='is null')
			self.assertIsNotNone(val, msg='is null2')




if __name__ == '__main__':
	unittest.main()
