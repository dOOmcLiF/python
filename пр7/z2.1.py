import pickle

data = {
    'name': 'Max',
    'age': 5,
    'breed': 'Labrador',
    'is_vaccinated': True
}

with open('dog_data.pkl', 'wb') as file:
    pickle.dump(data, file)

with open('dog_data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)