import os
import ConfigParser
import string




class Config(object):
	"""docstring for Config"""
	def __init__(self, subLocation):
		super(Config, self).__init__()
		self.configFileLocation = os.getcwd() + '/' + subLocation + '/config.ini'
		self.configSection 		= 'KeyValuePairs'
		self.config 			= ConfigParser.ConfigParser()
		self.config.read(self.configFileLocation)



	def Get(self, configKey):
		value = self.config.get(self.configSection, configKey)
		return value
	
