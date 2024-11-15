import shelve

with shelve.open('dog_shelve') as db:
    db['dog1'] = {'name': 'Max', 'age': 5, 'breed': 'Labrador'}
    db['dog2'] = {'name': 'Bella', 'age': 3, 'breed': 'Beagle'}

with shelve.open('dog_shelve') as db:
    dog1 = db['dog1']
    dog2 = db['dog2']
    print(dog1)
    print(dog2)
