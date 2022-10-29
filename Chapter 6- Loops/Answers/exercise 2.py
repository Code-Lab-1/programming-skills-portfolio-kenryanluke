ages = "\nHow old are you?"
ages += "\nEnter 'Quit' when you are finshed: "

while True:
  age = input(ages)
  if age == "Quit":
    break
  age = int(age)


  if age<3: 
    print("The ticket is free")
  elif age>3 and age<12:
    print("The ticket is 10")
  else:
    print("The ticket is 15")