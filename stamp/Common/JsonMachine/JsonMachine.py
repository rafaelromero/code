import json



class JsonMachine(object):

	def __init__(self):
			self.name = ''

	def EncodeCustomObject(self, obj):	
		actionsString = json.dumps(obj, default=convert_to_builtin_type, sort_keys=False)
		return actionsString

def convert_to_builtin_type(obj):
		return (obj.__dict__)

