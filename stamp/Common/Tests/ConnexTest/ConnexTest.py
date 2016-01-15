import os
import unittest
import Config
import Connex
from pymongo import MongoClient


class ConnexTest(unittest.TestCase):
	#"""docstring for ClassName"""
	#def __init__(self, arg):
	#	super(PackageTrackerIntegrationControllerTest, self).__init__()
	#	self.arg = arg


		def test_BuildConnex_Successfull(self):
			config = Config.Config('Tests/ConnexTest')
			connex = Connex.Connex(config)
			self.assertIsNotNone(config, msg='is null')



		def test_TestConnex_Successfull(self):
			config 		= Config.Config('Tests/ConnexTest')
			connex 		= Connex.Connex(config)
			mongoClient = connex.GetMongoClient()
			isConnected = mongoClient.alive  #connected ?
			#print mongoClient.port
			#print mongoClient.host
			#self.assertIsNotNone(config, msg='is null')
			self.assertTrue(isConnected, msg='is not connected')




if __name__ == '__main__':
	unittest.main()
