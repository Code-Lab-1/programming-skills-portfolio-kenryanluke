rivers = {'nile': 'egypt',
    'amazon': 'ecuador',
    'ganges': 'india',
    'mississippi': 'united states',
    'thame' : 'wiltshire',}

for river, country in rivers.items():
    print("The " + river.title() + " flows through " + country.title() + ".")

print("\nriver in this dictionary:")
for river in rivers.keys():
    print(river.title())

print("\ncountries in this dictionary:")
for country in rivers.values():
    print(country.title())