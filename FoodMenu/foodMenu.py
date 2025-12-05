
def display_time_menu():
    """Displays the time menu."""
    print('----------- Time ------------')
    print('Say Good Morning     (1)')
    print('Say Good AfterNoon   (2)')
    print('Say Good Evening     (3)')
    print('-----------------------------')


display_time_menu()

def get_user_time():
    time=int(input('Enter the Time: '))
    if time==1:
        print('\nGood Morning')
    elif time==2:
        print('\nGood AfterNoon')
    elif time==3:
        print('\nGood Evening')
    else:
        print("Invalid choice, please enter 1,2, or 3")

    return time

print('\n')
time=get_user_time()

if time==1:
    print('-------- Morning Time --------------')
    print('-------- Food Item ---------------')
    def foodItem():
        print("Drinks (1)")
        print("Snacks (2)")
        
        selectUser=int(input("enter your choice: "))
        if selectUser == 1: 
            print("you selected Drinks")
            
        elif selectUser == 2:
            print("you selected Snacks")
        else:
            print("Invalid choice, please enter 1,2 or 3")

        
        if selectUser == 1:
            print("Drinks")
            drinkList = ["Tea", "Coffee", "Cold drinks"]

            for i in range(len(drinkList)):
                print(i+1, drinkList[i])
           
            def get_user_drink():
                drink=int(input('Enter the Drink:'))
                if drink==1:
                    print('Tea')
                    
                    teaList = ["Black Tea", "Green Tea", "Masala Tea", "Ginger Tea","Brown Tea", "White Tea", "Herbal Tea", "Oolong Tea", "Rooibos Tea"]
                    teaPriceList = [46, 34, 10, 16]
                    for i in range(len(teaList)):
                        print(i+1, teaList[i], "------------ Rs.", teaPriceList[i])

                    selectUser=int(input("enter your choice: "))
                    if selectUser == 1:
                        print("you selected Black Tea")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * teaPriceList[0]
                        print("--------------------------------")
                        print("item: ", teaList[0])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", teaPriceList[0])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    elif selectUser == 2:
                        print("you selected Green Tea")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * teaPriceList[1]
                        print("--------------------------------")
                        print("item: ", teaList[1])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", teaPriceList[1])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    elif selectUser == 3:
                        print("you selected Masala Tea")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * teaPriceList[2]
                        print("--------------------------------")
                        print("item: ", teaList[2])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", teaPriceList[2])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    elif selectUser == 4:
                        print("you selected Ginger Tea")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * teaPriceList[3]
                        print("--------------------------------")
                        print("item: ", teaList[3])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", teaPriceList[3])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    else:
                        print("Invalid choice, please enter 1,2,3, or 4")
                

                elif drink==2:
                    print('Coffee')
                    coffeeList = ["Black Coffee", "Cappuccino", "Latte", "Espresso"]
                    coffeePriceList = [70, 125, 215, 121]
                    for i in range(len(coffeeList)):
                        print(i+1, coffeeList[i], "------------ Rs.", coffeePriceList[i])

                    selectUser=int(input("enter your choice: "))
                    if selectUser == 1:
                        print("you selected Black Coffee")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * coffeePriceList[0]
                        print("--------------------------------")
                        print("item: ", coffeeList[0])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", coffeePriceList[0])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    elif selectUser == 2:
                        print("you selected Cappuccino")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * coffeePriceList[1]
                        print("--------------------------------")
                        print("item: ", coffeeList[1])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", coffeePriceList[1])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    elif selectUser == 3:
                        print("you selected Latte")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * coffeePriceList[2]
                        print("--------------------------------")
                        print("item: ", coffeeList[2])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", coffeePriceList[2])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    elif selectUser == 4:
                        print("you selected Espresso")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * coffeePriceList[3]
                        print("--------------------------------")
                        print("item: ", coffeeList[3])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", coffeePriceList[3])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    else:
                        print("Invalid choice, please enter 1,2,3, or 4")
                elif drink==3:
                    print("cold drinks")
                    coldDrinkList = ["Coca Cola", "Pepsi", "Sprite", "Fanta"]
                    coldDrinkPriceList = [20, 30, 40, 50]
                    for i in range(len(coldDrinkList)):
                        print(i+1, coldDrinkList[i], "------------ Rs.", coldDrinkPriceList[i])
                    selectUser=int(input("enter your choice: "))
                    if selectUser == 1:
                        print("you selected Coca Cola")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * coldDrinkPriceList[0]
                        print("--------------------------------")
                        print("item: ", coldDrinkList[0])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", coldDrinkPriceList[0])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    elif selectUser == 2:
                        print("you selected Pepsi")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * coldDrinkPriceList[1]
                        print("--------------------------------")
                        print("item: ", coldDrinkList[1])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", coldDrinkPriceList[1])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    elif selectUser == 3:
                        print("you selected Sprite")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * coldDrinkPriceList[2]
                        print("--------------------------------")
                        print("item: ", coldDrinkList[2])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", coldDrinkPriceList[2])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    elif selectUser == 4:
                        print("you selected Fanta")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * coldDrinkPriceList[3]
                        print("--------------------------------")
                        print("item: ", coldDrinkList[3])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", coldDrinkPriceList[3])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")

                else:
                    print("Invalid choice, please enter 1,2 or 3")
                return drink
            print('\n')
            drink=get_user_drink()
            print('\n')
            print('Enjoy your Drink')
        elif selectUser == 2:
            print("Snacks")

            snackList = ["Biscuits", "Chips", "Cookies", "Crackers"]
            
            for i in range(len(snackList)):
                print(i+1, snackList[i])

            def get_user_snack():
                snack=int(input('Enter the Snack:'))
                if snack==1:
                    print('Biscuits')
                    biscuitsList= ["Almond Biscuits", "Eggless Almond Biscuits",
                                   "Chocolate Coated Biscuits"]
                    
                    biscuitsPriceList= [235, 432, 219]
                    
                    for i in range(len(biscuitsList)):
                        print(i+1, biscuitsList[i], "------------ Rs.", biscuitsPriceList[i])

                    selectUser=int(input("enter your choice: "))
                    if selectUser == 1: 
                        print("you selected Almond Biscuits")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * biscuitsPriceList[0]
                        print("--------------------------------")
                        print("item: ", biscuitsList[0])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", biscuitsPriceList[0])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    elif selectUser == 2:
                        print("you selected Eggless Almond Biscuits")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * biscuitsPriceList[1]
                        print("--------------------------------")
                        print("item: ", biscuitsList[1])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", biscuitsPriceList[1])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    elif selectUser == 3:
                        print("you selected Chocolate Coated Biscuits")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * biscuitsPriceList[2]
                        print("--------------------------------")
                        print("Total Amount: Rs.", totalAmount)
                        print("item: ", biscuitsList[2])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", biscuitsPriceList[2])
                        print("--------------------------------")
                    else:
                        print("Invalid choice, please enter 1,2, or 3")
                         
                elif snack==2:
                    print('Chips')
                    chipsList = ["Potato Chips", "Banana Chips", "Corn Chips"]
                    chipsPriceList = [10, 50, 150]
                    for i in range(len(chipsList)):
                        print(i+1, chipsList[i], "------------ Rs.", chipsPriceList[i])

                    selectUser=int(input("enter your choice: "))
                    if selectUser == 1:
                        print("you selected Potato Chips")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * chipsPriceList[0]
                        print("--------------------------------")
                        print("item: ", chipsList[0])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", chipsPriceList[0])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")

                    elif selectUser == 2:
                        print("you selected Banana Chips")
                        quantity=int(input("Enter the quantity: "))
                        totalAmount = quantity * chipsPriceList[1]
                        print("--------------------------------")
                        print("item: ", chipsList[1])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", chipsPriceList[1])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    
                    elif selectUser == 3:
                        print("you selected Corn Chips")
                        quantity=int(input("Enter the quantity: "))
                        totalAmount = quantity * chipsPriceList[2]
                        print("--------------------------------")
                        print("Total Amount: Rs.", totalAmount)
                        print("item: ", chipsList[2])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", chipsPriceList[2])
                        print("--------------------------------")
                    else:
                        print("Invalid choice, please enter 1,2, or 3")

                    


                elif snack==3:
                    print('Cookies')
                    cookiesList = ["Orange Cookies", "Double Choco Chip Cookies"]
                    cookiesPriceList = [50, 127]
                    for i in range(len(cookiesList)):
                        print(i+1, cookiesList[i], "------------ Rs.", cookiesPriceList[i])
                   
                    selectUser=int(input("enter your choice: "))
                    if selectUser == 1:
                        print("you selected Orange Cookies")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * cookiesPriceList[0]
                        print("--------------------------------")
                        print("item: ", cookiesList[0])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", cookiesPriceList[0])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")

                    elif selectUser == 2:
                        print("you selected Double Choco Chip Cookies")
                        quantity=int(input("Enter the quantity: "))
                        totalAmount = quantity * cookiesPriceList[1]
                        print("--------------------------------")
                        print("item: ", cookiesList[1])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", cookiesPriceList[1])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    else:
                        print("Invalid choice, please enter 1, or 2")
                
                elif snack==4:
                    print('Crackers')
                    crackersList = ["Cheese Crackers",
                                    "Ragi Crackers", "Black Pepper Sourdough Crackers",
                                    "Sweet Sesame Crackers"]
                    crackerPriceList = [320,543,365,343]

                    for i in range(len(crackersList)):
                        print(i+1, crackersList[i],"------------- Rs.", crackerPriceList[i])
                    
                    selectUser=int(input("enter your choice: "))

                    if selectUser == 1:
                        print("you selected Cheese Crackers")
                        quantity=int(input("Enter the quantity: "))
                        totalAmount = quantity * crackerPriceList[0]
                        print("--------------------------------")
                        print("item: ", crackersList[0])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", crackerPriceList[0])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    elif selectUser == 2:
                        print("you selected Ragi Crackers")
                        quantity=int(input("Enter the quantity: "))
                        totalAmount = quantity * crackerPriceList[1]
                        print("--------------------------------")
                        print("item: ", crackersList[1])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", crackerPriceList[1])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    elif selectUser == 3:
                        print("you selected Black Pepper Sourdough Crackers")
                        quantity=int(input("Enter the quantity: "))
                        totalAmount = quantity * crackerPriceList[2]
                        print("--------------------------------")
                        print("item: ", crackersList[2])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", crackerPriceList[2])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    elif selectUser == 4:
                        print("you selected Sweet Sesame Crackers")
                        quantity=int(input("Enter the quantity: "))
                        totalAmount = quantity * crackerPriceList[3]
                        print("--------------------------------")
                        print("item: ", crackersList[3])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", crackerPriceList[3])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    
                else:
                    print("Invalid choice, please enter 1,2,3 or 4")
                return snack
            print('\n')
            snack=get_user_snack()
            print('\n')
            print('Enjoy your Snack')
        else:
            print("Invalid choice, please enter 1, or 2")

        

    foodItem()

if time==2:
    print("-----------Afternoon Time-----------")
    print("----------Food Item----------------")
    def foodItem():
        print("chinise dish (1)")
        print("south dish (2)")

        selectUser=int(input("enter your choice: "))
        if selectUser == 1:
            print("you selected chinise")
        elif selectUser == 2:
            print("you selected south dish")
        else:
            print("Invalid choice, please enter 1, or 2")

        if selectUser == 1:
            print("chinise")

            chiniseList=["Noodles", "Pizza", "Burger","Momos", "Spring Roll", "Manchurian", "Fried Rice"]

            for i in range(len(chiniseList)):
                print(i+1, chiniseList[i])

            def get_user_chinise():
                chinise=int(input('Enter the chinise:'))
                if chinise==1:
                    print('Noodles')
                    noodlesList = ["Chowmein", "Hakka Noodles", "Veg Noodles"]
                    noodlesPriceList = [150, 200, 250]
                    for i in range(len(noodlesList)):
                        print(i+1, noodlesList[i], "------------ Rs.", noodlesPriceList[i])

                    selectUser=int(input("enter your choice: "))
                    if selectUser == 1:
                        print("you selected Chowmein")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * noodlesPriceList[0]
                        print("--------------------------------")
                        print("item: ", noodlesList[0])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", noodlesPriceList[0])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    elif selectUser == 2:
                        print("you selected Hakka Noodles")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * noodlesPriceList[1]
                        print("--------------------------------")
                        print("item: ", noodlesList[1])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", noodlesPriceList[1])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    elif selectUser == 3:
                        print("you selected Veg Noodles")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * noodlesPriceList[2]
                        print("--------------------------------")
                        print("item: ", noodlesList[2])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", noodlesPriceList[2])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    else:
                        print("Invalid choice, please enter 1,2, or 3")

                elif chinise==2:
                    print('Pizza')
                    pizzaList = ["Cheese Pizza", "Veg Pizza", "Paneer Pizza"]
                    pizzaPriceList = [250, 300, 350]
                    for i in range(len(pizzaList)):
                        print(i+1, pizzaList[i], "------------ Rs.", pizzaPriceList[i])

                    selectUser=int(input("enter your choice: "))
                    if selectUser == 1:
                        print("you selected Cheese Pizza")
                        quantity=int(input("Enter the quantity: "))
                        totalAmount = quantity * pizzaPriceList[0]  
                        print("--------------------------------")
                        print("item: ", pizzaList[0])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", pizzaPriceList[0])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    elif selectUser == 2:
                        print("you selected Veg Pizza")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * pizzaPriceList[1]
                        print("--------------------------------")
                        print("item: ", pizzaList[1])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", pizzaPriceList[1])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    elif selectUser == 3:
                        print("you selected Paneer Pizza")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * pizzaPriceList[2]
                        print("--------------------------------")
                        print("item: ", pizzaList[2])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", pizzaPriceList[2])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    else:
                        print("Invalid choice, please enter 1,2, or 3")
                elif chinise==3:
                    print('Burger')
                    burgerList = ["Cheese Burger", "Veg Burger", "Paneer Burger"]
                    burgerPriceList = [150, 200, 250]
                    for i in range(len(burgerList)):
                        print(i+1, burgerList[i], "------------ Rs.", burgerPriceList[i])

                    selectUser=int(input("enter your choice: "))
                    if selectUser == 1:
                        print("you selected Cheese Burger")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * burgerPriceList[0]
                        print("--------------------------------")
                        print("item: ", burgerList[0])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", burgerPriceList[0])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    elif selectUser == 2:
                        print("you selected Veg Burger")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * burgerPriceList[1]
                        print("--------------------------------")
                        print("item: ", burgerList[1])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", burgerPriceList[1])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    elif selectUser == 3:
                        print("you selected Paneer Burger")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * burgerPriceList[2]
                        print("--------------------------------")
                        print("item: ", burgerList[2])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", burgerPriceList[2])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    else:
                        print("Invalid choice, please enter 1,2, or 3")
                else:
                    print("Invalid choice, please enter 1,2 or 3")
                return chinise
            print('\n')
            chinise=get_user_chinise()
            print('\n')
            print('Enjoy your chinise')
        elif selectUser == 2:
            print("south dish")

            southDishList=["Idli", "Dosa", "Uttapam"]

            for i in range(len(southDishList)):
                print(i+1, southDishList[i])

            def get_user_south_dish():
                southDish=int(input('Enter the south dish:'))
                if southDish==1:
                    print('Idli')
                    idliList = ["Plain Idli", "Masala Idli", "Sambar Idli"]
                    idliPriceList = [50, 70, 90]
                    for i in range(len(idliList)):
                        print(i+1, idliList[i], "------------ Rs.", idliPriceList[i])

                    selectUser=int(input("enter your choice: "))
                    if selectUser == 1:
                        print("you selected Plain Idli")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * idliPriceList[0]
                        print("--------------------------------")
                        print("item: ", idliList[0])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", idliPriceList[0])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    elif selectUser == 2:
                        print("you selected Masala Idli")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * idliPriceList[1]
                        print("--------------------------------")
                        print("item: ", idliList[1])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", idliPriceList[1])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    elif selectUser == 3:
                        print("you selected Sambar Idli")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * idliPriceList[2]
                        print("--------------------------------")
                        print("item: ", idliList[2])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", idliPriceList[2])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    else:
                        print("Invalid choice, please enter 1,2, or 3")

                elif southDish==2:
                    print('Dosa')
                    dosaList = ["Plain Dosa", "Masala Dosa", "Onion Dosa"]
                    dosaPriceList = [50, 70, 90]
                    for i in range(len(dosaList)):
                        print(i+1, dosaList[i], "------------ Rs.", dosaPriceList[i])   
                    selectUser=int(input("enter your choice: "))
                    if selectUser == 1:
                        print("you selected Plain Dosa")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * dosaPriceList[0]
                        print("--------------------------------")
                        print("item: ", dosaList[0])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", dosaPriceList[0])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    elif selectUser == 2:
                        print("you selected Masala Dosa")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * dosaPriceList[1]
                        print("--------------------------------")
                        print("item: ", dosaList[1])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", dosaPriceList[1])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    elif selectUser == 3:
                        print("you selected Onion Dosa")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * dosaPriceList[2]
                        print("--------------------------------")
                        print("item: ", dosaList[2])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", dosaPriceList[2])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    else:
                        print("Invalid choice, please enter 1,2, or 3")
                elif southDish==3:
                    print('Uttapam')
                    uttapamList = ["Plain Uttapam", "Masala Uttapam", "Onion Uttapam"]
                    uttapamPriceList = [50, 70, 90]
                    for i in range(len(uttapamList)):
                        print(i+1, uttapamList[i], "------------ Rs.", uttapamPriceList[i])   
                    selectUser=int(input("enter your choice: "))
                    if selectUser == 1:
                        print("you selected Plain Uttapam")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * uttapamPriceList[0]
                        print("--------------------------------")
                        print("item: ", uttapamList[0])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", uttapamPriceList[0])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    elif selectUser == 2:
                        print("you selected Masala Uttapam")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * uttapamPriceList[1]
                        print("--------------------------------")
                        print("item: ", uttapamList[1])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", uttapamPriceList[1])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    elif selectUser == 3:
                        print("you selected Onion Uttapam")
                        quantity=int(input("Enter the quantity: "))       
                        totalAmount = quantity * uttapamPriceList[2]
                        print("--------------------------------")
                        print("item: ", uttapamList[2])
                        print("Quantity: ", quantity)
                        print("Price: Rs.", uttapamPriceList[2])
                        print("Total Amount: Rs.", totalAmount)
                        print("--------------------------------")
                    else:
                        print("Invalid choice, please enter 1,2, or 3") 
                else:
                    print("Invalid choice, please enter 1,2 or 3")
                return southDish
            print('\n')
            southDish=get_user_south_dish()
            print('\n')
            print('Enjoy your south dish')
        else:
            print("Invalid choice, please enter 1, or 2")
        return selectUser
    print('\n')
    

            
        
    foodItem()

if time==3:
    print("--------------Evening Time-------------")
    print("--------------Food Item----------------")
    def foodItem():
        print("special thali (1)")
        print("normal thali (2)")

        selectUser=int(input("enter your choice: "))
        if selectUser == 1:
            print("you selected special thali")
        elif selectUser == 1:
            print("you selected normal thali")
        else:
            print("Invalid choice, please enter 1, or 2")

        if selectUser == 1:
            print("special thali")

            specialThaliList=["Paneer Butter Masala", "Dal Makhani", "Chole Bhature"]
            specialThaliPriceList=[250, 200, 150]
            for i in range(len(specialThaliList)):
                print(i+1, specialThaliList[i], "------------ Rs.", specialThaliPriceList[i])
            selectUser=int(input("enter your choice: "))
            if selectUser == 1:
                print("you selected Paneer Butter Masala")
                quantity=int(input("Enter the quantity: "))       
                totalAmount = quantity * specialThaliPriceList[0]
                print("--------------------------------")
                print("item: ", specialThaliList[0])
                print("Quantity: ", quantity)
                print("Price: Rs.", specialThaliPriceList[0])
                print("Total Amount: Rs.", totalAmount)
                print("--------------------------------")
            elif selectUser == 2:
                print("you selected Dal Makhani")
                quantity=int(input("Enter the quantity: "))       
                totalAmount = quantity * specialThaliPriceList[1]
                print("--------------------------------")
                print("item: ", specialThaliList[1])
                print("Quantity: ", quantity)
                print("Price: Rs.", specialThaliPriceList[1])
                print("Total Amount: Rs.", totalAmount)
                print("--------------------------------")
            elif selectUser == 3:
                print("you selected Chole Bhature")
                quantity=int(input("Enter the quantity: "))       
                totalAmount = quantity * specialThaliPriceList[2]
                print("--------------------------------")
                print("item: ", specialThaliList[2])
                print("Quantity: ", quantity)
                print("Price: Rs.", specialThaliPriceList[2])
                print("Total Amount: Rs.", totalAmount)
                print("--------------------------------")
            else:
                print("Invalid choice, please enter 1,2, or 3")
        elif selectUser == 2:
            print("normal thali")

            normalThaliList=["Dal Fry", "Paneer Tikka", "Veg Biryani"]
            normalThaliPriceList=[150, 200, 250]
            for i in range(len(normalThaliList)):
                print(i+1, normalThaliList[i], "------------ Rs.", normalThaliPriceList[i])
            selectUser=int(input("enter your choice: "))
            if selectUser == 1:
                print("you selected Dal Fry")
                quantity=int(input("Enter the quantity: "))       
                totalAmount = quantity * normalThaliPriceList[0]
                print("--------------------------------")
                print("item: ", normalThaliList[0])
                print("Quantity: ", quantity)
                print("Price: Rs.", normalThaliPriceList[0])
                print("Total Amount: Rs.", totalAmount)
                print("--------------------------------")
            elif selectUser == 2:
                print("you selected Paneer Tikka")
                quantity=int(input("Enter the quantity: "))       
                totalAmount = quantity * normalThaliPriceList[1]
                print("--------------------------------")
                print("item: ", normalThaliList[1])
                print("Quantity: ", quantity)
                print("Price: Rs.", normalThaliPriceList[1])
                print("Total Amount: Rs.", totalAmount)
                print("--------------------------------")
            elif selectUser == 3:
                print("you selected Veg Biryani")
                quantity=int(input("Enter the quantity: "))       
                totalAmount = quantity * normalThaliPriceList[2]
                print("--------------------------------")
                print("item: ", normalThaliList[2])
                print("Quantity: ", quantity)
                print("Price: Rs.", normalThaliPriceList[2])
                print("Total Amount: Rs.", totalAmount)
                print("--------------------------------")
            else:
                print("Invalid choice, please enter 1,2, or 3")
        else:
            print("Invalid choice, please enter 1, or 2")

        
            
    foodItem()

    
