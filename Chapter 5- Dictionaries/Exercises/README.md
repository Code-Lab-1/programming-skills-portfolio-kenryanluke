# Chapter 5 Exercises

Exercises with a tick mark :ballot_box_with_check: represent exercises that must be submitted as part of your Programming Skills Portfolio as a minimum expectation. Completing more exercises provides the opportunity to attain higher marks. For each exercise you should create a _**new project**_ with the name of the exercise and save it to this exercises folder in your local repository.

Once you have completed your solution you should make sure you commit and push your solutions to your remote repository on GitHub. You can commit and push as many changes to your solutions as you wish, only those pushed before the chapter deadlines will be marked for the Programming Skills Portfolio.  

---
&nbsp;

## Exercise 1: Person :ballot_box_with_check:

Use a dictionary to store information about a person you know.Store their first name, last name, age, and the city in which they live. You

should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

info = {"first_name":"Theo", "last_name":"Alemania", "age":"17", "city":"Roxas City"}

print(info["first_name"])

print(info["last_name"])

print(info["age"])


print(info["city"])

&nbsp;
&nbsp;

## Exercise 2: Glossary :ballot_box_with_check:

A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

* Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store 

their meanings as values.

* Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print 

the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between 

each word-meaning pair in your output.

glossary = {"print":"Is a function which prints a specified message to the screen",
            "variable":"reserved memory location to store values", 
            "list":"data structure in Python that is a mutable, or changeable, ordered sequence of elements", 
            "conditional statements":"used to handle conditions in your program", 
            "integer":"is a whole number, positive or negative, without decimals, of unlimited length."}

key = 'print'
print("\n" + key.title() + ": " + glossary[key])
key = 'variable'
print("\n" + key.title() + ": " + glossary[key])
key = 'list'
print("\n" + key.title() + ": " + glossary[key])
key = 'conditional statements'
print("\n" + key.title() + ": " + glossary[key])
key = 'integer'
print("\n" + key.title() + ": " + glossary[key])


&nbsp;
&nbsp;

## Exercise 3: Glossary 2 :ballot_box_with_check:
Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()

calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 

to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.

glossary = {"print":"Is a function which prints a specified message to the screen",
            "variable":"reserved memory location to store values", 
            "list":"data structure in Python that is a mutable, or changeable, ordered sequence of elements", 
            "conditional statements":"used to handle conditions in your program", 
            "integer":"is a whole number, positive or negative, without decimals, of unlimited length.",
            "float":"a method that returns a floating-point number for a provided number or string",
            "pop":"removes the specified item from the dictionary",
            "loop":"repeating something over and over until a particular condition is satisfied.",
            "string":"a collection of alphabets, words or other characters",
            "boolean":"used to represent the truth value of an expression."}

for key, definition in glossary.items():
    print("\n" + key.title() + ": " + definition)

&nbsp;
&nbsp;

## Exercise 4: Rivers :ballot_box_with_check:

Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

* Use a loop to print the name of each river included in the dictionary.

* Use a loop to print the name of each country included in the dictionary.

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
&nbsp;
&nbsp;

## Exercise 5: Pets :ballot_box_with_check:

Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the

owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about 

each pet

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

&nbsp;
&nbsp;


