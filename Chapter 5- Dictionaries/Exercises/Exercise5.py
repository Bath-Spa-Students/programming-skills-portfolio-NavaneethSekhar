Pets = []

Pet = {
    'species': 'Orangatang',
    'name': 'Moonshine',
    'owner': 'Linda',
    'weight': 90,
    'eats': 'Fruits',
}
Pets.append(Pet)

Pet = {
    'species': 'Sugar Glider',
    'name': 'Jumpsuit',
    'owner': 'Casandra',
    'weight': 0.5,
    'eats': 'Bugs',
}
Pets.append(Pet)

Pet = {
    'species': 'dog',
    'name': 'Ying',
    'owner': 'Mila',
    'weight': 40,
    'eats': 'pillows',
}
Pets.append(Pet)

for Pet in Pets:
    print("\nThis is the knowledge I have about " + Pet['name'].title() + ":")
    for key, value in Pet.items():
        print("\t" + key + ": " + str(value))