from mongoengine import *
connect('store', host='localhost', port=27017)

class Stock(Document):
  id = 
  name = StringField(required=True, max_length=200)
  price = DecimalField(required=True)
  description = StringField(required=False)

def create(name, price, description = ''):
  pass

def read_all():
  pass

def read_one(name)
  pass

def update(id, name, price, description):
  pass

def delete(id):
  pass



