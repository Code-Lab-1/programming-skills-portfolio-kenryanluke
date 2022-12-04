products = """
Products:
Beverages------------------------------------------
Code:                                Stock:
   A1 - Bottle of Water = 1AED       5
   B1 - Can of Pepsi = 2.5AED        0
   C1 - Can of Sprite = 2.5AED       4
   D1 - Can of Coke = 2.5AED         3
   E1 - Iced Coffee = 8AED           8
   F1 - Iced tea = 3.5AED            2

Snacks-----------------------------------------------
   A2 - Small Doritos = 4AED         0
   B2 - Small Lays chips = 3.5AED    3
   C2 - Croissant = 3AED             5
   D2 - Muffin = 5AED                3
   E2 - Turkey Ham sandwich = 10AED  2
   F2 - Tuna Sandwich = 10AED        8
"""
print(products) #Prints the Vending Machine's menu


#Price
water = 1
pepsi = float(2.5)
sprite = float(2.5)
coke = float(2.5)
coffee = 8
tea = float(3.5)

doritos = 4
lays = float(3.5)
croissant = float(3)
muffin = 5
turkey = 10
tuna = 10

#Variables set for the products' prices


money_in = float(input("Insert cash: "))
print("\nAmount of money received:", money_in)
prdct_code = input("Enter product code: ")

#Prints the message to enter cash and input code and which runs the selected code's function






#Bevs
def A1():
    water_stock = 1
    if water_stock != 0: #If stock is not equal to 0, it will continue with the program, else it stops and prints "Out of stock"
     if money_in >= water: #When the amount of money inputed is greater than the price of product, it will proceed with the program, else it tells the user how much more money is needed
         change = money_in - water
         print("\nDispensing Bottle of Water")
         print("Your change is" , change)
         water_stock -= 1   #Takes away 1 stock when dispensed
         print("Stock left:", water_stock) #Prints the stock after product is dispensed
     else:
         remain = water - money_in 
         print("Cash insufficient. Amount pending:", remain) #Shows how much money is pending
    else:
        print("Out of Stock")


def B1():
    pepsi_stock = 0
    if pepsi_stock != 0:
     if money_in >= pepsi:
         change = money_in - pepsi
         print("\nDispensing Can of Sprite")
         print("Your change is" , change)
         pepsi_stock -= 1
         print("Stock left:", pepsi_stock)
     else:
         remain = pepsi - money_in
         print("Cash insufficient. Amount pending:", remain)
    else:
        print("Out of Stock")
        
        
def C1():
    sprite_stock = 4
    if sprite_stock != 0:
     if money_in >= sprite:
         change = money_in - sprite
         print("\nDispensing Can of Sprite")
         print("Your change is" , change)
         sprite_stock -= 1
         print("Stock left:", sprite_stock)
     else:
         remain = sprite - money_in
         print("Cash insufficient. Amount pending:", remain)
    else:
        print("Out of Stock")

def D1():
    coke_stock = 3
    if coke_stock != 0:
     if money_in >= coke:
         change = money_in - coke
         print("\nDispensing Can of Coke")
         print("Your change is" , change)
         coke_stock -= 1
         print("Stock left:", coke_stock)
     else:
         remain = coke - money_in
         print("Cash insufficient. Amount pending:", remain)
    else:
        print("Out of Stock")

def E1():
    coffee_stock = 8
    if coffee_stock != 0:
     if money_in >= coffee:
         change = money_in - coffee
         print("\nDispensing Can of Coffee")
         print("Your change is" , change)
         coke_stock -= 1
         print("Stock left:", coke_stock)
     else:
         remain = coffee - money_in
         print("Cash insufficient. Amount pending:", remain)
    else:
        print("Out of Stock")

def F1():
    tea_stock = 2
    if tea_stock != 0:
     if money_in >= tea:
         change = money_in - tea
         print("\nDispensing Can of Iced Tea")
         print("Your change is" , change)
         tea_stock -= 1
         print("Stock left:", tea_stock)
     else:
         remain = coke - money_in
         print("Cash insufficient. Amount pending:", remain)
    else:
        print("Out of Stock")


#Food
def A2():
    doritos_stock = 0
    if doritos_stock != 0:
     if money_in >= doritos:
         change = money_in - doritos
         print("\nDispensing a Bag of Doritos")
         print("Your change is" , change)
         doritos_stock -= 1
         print("Stock left:", doritos_stock)
     else:
         remain = doritos - money_in
         print("Cash insufficient. Amount pending:", remain)
    else:
        print("Out of Stock")

def B2():
    lays_stock = 3
    if lays_stock != 0:
     if money_in >= lays:
         change = money_in - lays
         print("\nDispensing a Bag of Lays Chips")
         print("Your change is" , change)
         laysr_stock -= 1
         print("Stock left:", lays_stock)
     else:
         remain = lays - money_in
         print("Cash insufficient. Amount pending:", remain)
    else:
        print("Out of Stock")

def C2():
    croissant_stock = 5
    if croissant_stock != 0:
     if money_in >= croissant:
         change = money_in - croissant
         print("\nDispensing a Croissant")
         print("Your change is" , change)
         croissant_stock -= 1
         print("Stock left:", croissant_stock)
     else:
         remain = croissant - money_in
         print("Cash insufficient. Amount pending:", remain)
    else:
        print("Out of Stock")

def D2():
    muffin_stock = 3
    if muffin_stock != 0:
     if money_in >= muffin:
         change = money_in - muffin
         print("\nDispensing a Muffin")
         print("Your change is" , change)
         muffin_stock -= 1
         print("Stock left:", muffin_stock)
     else:
         remain = muffin - money_in
         print("Cash insufficient. Amount pending:", remain)
    else:
        print("Out of Stock")
    
def E2():
    turkey_stock = 2
    if turkey_stock != 0:
     if money_in >= turkey:
         change = money_in - turkey
         print("\nDispensing a Turkey Ham Sandwich")
         print("Your change is" , change)
         turkey_stock -= 1
         print("Stock left:", turkey_stock)
     else:
         remain = turkey - money_in
         print("Cash insufficient. Amount pending:", remain)
    else:
        print("Out of Stock")

def F2():
    tuna_stock = 0
    if tuna_stock != 0:
     if money_in >= tuna:
         change = money_in - tuna
         print("\nDispensing a Tuna Sandwish")
         print("Your change is" , change)
         tuna_stock -= 1
         print("Stock left:", tuna_stock)
     else:
         remain = tuna - money_in
         print("Cash insufficient. Amount pending:", remain)
    else:
        print("Out of Stock")


        

    

if prdct_code == "A1":
    A1()
elif prdct_code == "B1":
    B1()
elif prdct_code == "C1":
    C1()
elif prdct_code == "D1":
    D1()
elif prdct_code == "E1":
    E1()
elif prdct_code == "F1":
    F1()
elif prdct_code == "A2":
    A2()
elif prdct_code == "B2":
    B2()
elif prdct_code == "C2":
    C2()
elif prdct_code == "D2":
    D2()
elif prdct_code == "E2":
    E2()
elif prdct_code == "F2":
    F2()

#Conditional statement using if elif to match the product code, each statement runs the function
