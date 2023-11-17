sandwich_orders = ["Cheese pimiento", "Grilled Cheese", "Tuna Sandwich"]
finished_sandwiches = []

while sandwich_orders:
    sandwich_popped= sandwich_orders.pop()
    print("I'm working on your " + sandwich_popped + " sandwich.")
    finished_sandwiches.append(sandwich_popped)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")