toppings = "\nWhich toppings would you like on your pizza?"
toppings += "\nEnter 'Quit' when you have selected everything: "

while True:
    topping = input(toppings)
    if topping != 'Quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
      break