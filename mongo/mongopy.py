from pymongo import MongoClient



connection = MongoClient("mongodb://localhost");

db = connection.shoes.shoes;




results = db.find();


for record in results:
	print(record['name'] + ',' + ',' + record['color'] + ',' + str(record['size']))


	connection.close();
