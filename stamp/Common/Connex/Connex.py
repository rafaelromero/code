from pymongo import MongoClient
import Config



class Connex(object):
	"""docstring for Connex"""
	def __init__(self, config):
		super(Connex, self).__init__()
		self.config = config
		self.mongoClient = None



	def GetMongoClient(self):
		if (self.mongoClient == None or self.mongoClient.alive == False):
			self.mongoClient = MongoClient(self.config.Get('mongoserveraddress'), int(self.config.Get('mongoserverport')))

		return self.mongoClient


		
