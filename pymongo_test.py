from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.testing_database
myFirstCollection = db.myFirstCollection

document = {
  "nam": "TOROMBOLO",
  "activitie": ["walk", "play", "run"]
}

try:
  myFirstCollection.insert_one(document)
  result = myFirstCollection.find()
  for document_extracted in result:
    print(document_extracted)
except Exception as error:
  print(error)




