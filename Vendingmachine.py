import time

products = """
Products:
Beverages--------------------------------------------
Code:                                
   A1 - Bottle of Water = 1AED       
   B1 - Can of Pepsi = 2.5AED        
   C1 - Can of Sprite = 2.5AED       
   D1 - Can of Coke = 2.5AED         
   E1 - Iced Coffee = 8AED          
   F1 - Iced tea = 3.5AED            

Snacks-----------------------------------------------
   A2 - Small Doritos = 4AED         
   B2 - Small Lays chips = 3.5AED    
   C2 - Croissant = 3AED             
   D2 - Muffin = 5AED                
   E2 - Turkey Ham sandwich = 10AED  
   F2 - Tuna Sandwich = 10AED        
-----------------------------------------------------
"""

print(products) #Prints the Vending Machine's menu


#Price
water = float(1)
pepsi = float(2.5)
sprite = float(2.5)
coke = float(2.5)
coffee = float(8)
tea = float(3.5)

doritos = float(4)
lays = float(3.5)
croissant = float(3)
muffin = float(5)
turkey = float(10)
tuna = float(10)

time.sleep(1)
#Variables set for the products' prices
que = False
while que == False:
    money_in = float(input("Insert cash: "))
    print("\nAmount of money received:", money_in)
    prdct_code = input("Enter product code: ")
    #Prints the message to enter cash and input code and which runs the selected code's function

    #Bevs
    def A1():
         if money_in >= water: #When the amount of money inputed is greater than the price of product, it will proceed with the program, else it tells the user how much more money is needed
            change = money_in - water
            print("\nDispensing a Bottle of Water ")
            print("Your change is" , change)               
         else:
            remain = water - money_in
            print("Cash insufficient. Amount pending:", remain) #Shows how much money is pending


    def B1():
         if money_in >= pepsi:
            change = money_in - pepsi
            print("\nDispensing Can of Pepsi")
            print("Your change is" , change)
         else:
            remain = pepsi - money_in
            print("Cash insufficient. Amount pending:", remain)
        
            
    def C1():
         if money_in >= sprite:
            change = money_in - sprite
            print("\nDispensing Can of Sprite")
            print("Your change is" , change)
         else:
            remain = sprite - money_in
            print("Cash insufficient. Amount pending:", remain)
        
    def D1():
         if money_in >= coke:
            change = money_in - coke
            print("\nDispensing Can of Coke")
            print("Your change is" , change)
         else:
            remain = coke - money_in
            print("Cash insufficient. Amount pending:", remain)
        
    def E1():
         if money_in >= coffee:
            change = money_in - coffee
            print("\nDispensing Can of Coffee")
            print("Your change is" , change)
         else:
            remain = coffee - money_in
            print("Cash insufficient. Amount pending:", remain)

    def F1():
         if money_in >= tea:
            change = money_in - tea
            print("\nDispensing Can of Iced Tea")
            print("Your change is" , change)
         else:
            remain = tea - money_in
            print("Cash insufficient. Amount pending:", remain)


    #Food
    def A2():
         if money_in >= doritos:
            change = money_in - doritos
            print("\nDispensing a Bag of Doritos")
            print("Your change is" , change)
         else:
            remain = doritos - money_in
            print("Cash insufficient. Amount pending:", remain)

    def B2():
         if money_in >= lays:
            change = money_in - lays
            print("\nDispensing a Bag of Lays Chips")
            print("Your change is" , change)
         else:
            remain = lays - money_in
            print("Cash insufficient. Amount pending:", remain)

    def C2():
         if money_in >= croissant:
            change = money_in - croissant
            print("\nDispensing a Croissant")
            print("Your change is" , change)
         else:
            remain = croissant - money_in
            print("Cash insufficient. Amount pending:", remain)

    def D2():
         if money_in >= muffin:
            change = money_in - muffin
            print("\nDispensing a Muffin")
            print("Your change is" , change)
         else:
            remain = muffin - money_in
            print("Cash insufficient. Amount pending:", remain)
        
    def E2():
         if money_in >= turkey:
            change = money_in - turkey
            print("\nDispensing a Turkey Ham Sandwich")
            print("Your change is" , change)
         else:
            remain = turkey - money_in
            print("Cash insufficient. Amount pending:", remain)

    def F2():
         if money_in >= tuna:
            change = money_in - tuna
            print("\nDispensing a Tuna Sandwish")
            print("Your change is" , change)
         else:
            remain = tuna - money_in
            print("Cash insufficient. Amount pending:", remain)


            

    time.sleep(1)   

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
    else:
        print('Code Invalid')
    
    time.sleep(1)
    if que == False:
        q = input('''\nWould you like to continue?
Input Yes to continue
Input No to quit:
''')
        if q == 'Yes':
            que = False
        elif q == 'No':
            que = True
            print('Thank you for purchasing')

#Conditional statement using if elif to match the product code, each statement runs the function
