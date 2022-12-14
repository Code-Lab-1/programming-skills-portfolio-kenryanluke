pets = []

pet = {'species': 'cat',
    'name': 'whisker',
    'owner': 'Theo',
    'weight': str(36)+ "kg",
    'eats': 'rats',}
pets.append(pet)

pet = {'species': 'parrot',
    'name': 'Rio',
    'owner': 'Bob',
    'weight': str(9)+ "kg",
    'eats': 'seeds',}
pets.append(pet)

pet = {'species': 'dog',
    'name': 'Bond',
    'owner': 'Anya',
    'weight': str(36)+ "kg",
    'eats': 'bones',}
pets.append(pet)

for pet in pets:
    print("\nAbout " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))