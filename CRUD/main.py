from mongoengine import *
import os

connect('store', host='localhost', port=27017)

class Stock(Document):
  name = StringField(required=True, max_length=200)
  price = DecimalField(required=True)
  description = StringField(required=False)

def create(name = '', price = 0.0, description = ''):
   new_document = Stock(name, price, description).save()
   print(new_document.to_json())

def read_all():
  for doc in Stock.objects:
    print(doc.to_json())

def read_first(name):
  document = Stock.objects(name = name)[0]
  print(document.to_json())

def update(id, name = '', price = '', description = ''):
  document = Stock.objects(id = id)[0]

  if name != '' and name != "''":
    document.update(name = name)
  if price != '' and price != "''":
    document.update(price = price)
  if description != '' and description != "''":
    document.update(description = description)
  document.reload()
  print(document.to_json())

def delete(id):
  document = Stock.objects(id = id)[0]
  print(document.to_json())
  return document.delete()

def get_input_and_execute(fn, input_string = 'none'):
  print('Imput expected: ', input_string)

  if input_string != 'none':
    user_fields = input()
    arguments = tuple(x.strip() for x in user_fields.split(','))
    return fn(*arguments)
  else:
    return fn()

def show_menu():
  print('[ 1 ] Create')
  print('[ 2 ] Read_all')
  print('[ 3 ] Read_first')
  print('[ 4 ] Update')
  print('[ 5 ] Delete')
  print('[ 6 ] Exit')

def crud_action(action):
  actionTuple = {
      '1': (create, 'name, price, description'),
      '2': (read_all,),
      '3': (read_first, 'name' ),
      '4': (update, 'id, name, price, description'),
      '5': (delete, 'id')
  }[action]
  return get_input_and_execute(*actionTuple)

while True:
  show_menu()
  try:
    action = input()
    if(action == '6'):
      break
    else:
      result = crud_action(action)
      print('')
  except Exception as error:
    print('Ups! something is wrong', error)
print('bye!')

