people = ["Yang, ", "Ryan, ", "Theo, "]

print("I have 2 spots for dinner, anyone willing to come?")

people.pop(1)
print("Im sorry Ryan, as I wont be able to invite you for dinner")

people.pop(1)

print("Im sorry Theo, as I wont be able to invite you for dinner")

print("Yang, you're still invited for dinner")

people.remove("Yang, ")

print(people)