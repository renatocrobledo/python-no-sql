from mongoengine import *

connect('test_database', host='localhost', port=27017)

class MySecondCollection(Document):
  title = StringField(required=True, max_length=200)
  content = StringField(required=True)
  author = StringField(required=False)

myNewDocument = MySecondCollection(
  title='Sample Post title',
  content='Some engaging content'
)

myNewDocument.save()

query_response = MySecondCollection.objects.first()
#print(dir(query_response))
#print(query_response.to_json())
print(query_response.id)
#for document in query_response:
#  print(document.title)