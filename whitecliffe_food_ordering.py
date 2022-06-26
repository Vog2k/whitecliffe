# Copyright 2022 by Nidhi Gowdra.
# All rights reserved.
# This file is part of the Whitecliffe Food Ordering System,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

import os

import Create_Order
from Create_Order import Create_Order

import Helper_Func
from Helper_Func import Helper_Func

Order_LIST = []
CREATE_FLAG = 1
OPTION_FLAG = 1

print("Welcome to the whitecliffe Food Ordering system") #This will be the header of the program

while OPTION_FLAG != 0:  # Option 0 sends the user back
    option = Helper_Func.Menu()

    if option == 1:  # if the user enters this number this part of the code will run
        while (CREATE_FLAG == 1):  # While loop until somthinig entered this loop will continue
            print("Please input Staff Name and press enter")
            ID = input()  # This section will need the user to enter a character or characters
            print("Please input the description of the order/s and press enter")
            print("[If you require a unique order token, input UOT and press enter]")
            Order_Desc = input() #requires the user to enter a number
            print("Please input your Name (optional) and press enter")
            Name = input()

            if Name == "":  # If the user does not enter a name the end will result in Not specified
                Name = "Not specified"

            Order = Create_Order(ID, Name, Order_Desc)

            if "UOT" in Order.Desc:  # This will give the user their new UOT number with hexadecimal
                Order = Helper_Func.UniqueToken(Order)
                Helper_Func.DisplayOrder(Order)
                Order_LIST.append(Order)
            else:
                Order_LIST.append(Order)

            print("Do you want to create another order? (Y/N)")
            user_in = input()
            if user_in == "N" or user_in == "n":  # This will appear when the user has completed a new ticket
                CREATE_FLAG = 0

    elif option == 2:
        for obj in Order_LIST:
            print("*******************")
            print("Order No: ", obj.OrderNo)
            print("ID: ", obj.ID)  # This will display all the information on the current ticket
            print("Name: ", obj.Name)
            print("Description of the order: ", obj.Desc)
            print("Order Status: ", obj.Order_STATUS)

            if obj.Response != "N/A":
                print("Response: ", obj.Response)
            print("*******************")

    elif option == 3:
        print("Please enter the Order number to respond: ")
        USER_IN_Order_NO = int(input())  # This will open up a current ticket in use, requesting a ticket number

        for obj in Order_LIST:
            if obj.OrderNo == USER_IN_Order_NO:
                print("Please enter the response for the Order No: ", obj.OrderNo)
                RESPONSE_INPUT = input()
                obj.Response = RESPONSE_INPUT  # This will be activated once the user has entered a response
                obj.Order_STATUS = "Closed"  # After the response has been given the ticket status will close

    elif option == 4:
        print("Please enter the Order number to reopen: ")
        USER_IN_Order_NO = int(input())
        # This will re open an exiting ticket that you can edit again
        for obj in Order_LIST:
            if obj.OrderNo == USER_IN_Order_NO:
                if obj.Order_STATUS == "Closed":
                    obj.Order_STATUS = "Reopened"
                    print("Please enter the description for the Order No: ", obj.OrderNo)
                    print("[If you require a unique order token, input UOT and press enter]")
                    Order_Desc = input()
                    obj.Desc = Order_Desc
                    if "UOT" in obj.Desc:
                        TK = Helper_Func.UniqueToken(obj)
                        Helper_Func.DisplayOrder(TK)

    elif option == 5:
        print("Displaying Order statistics")
        C, F, R = Create_Order.Stats(Order_LIST)

        print("++++++++++++++++++++++++++++")
        print("Created: ", C)
        print("Finished: ", F)  # These three characters represent Created Finished and Remaining
        print("Remaining: ", R)
        print("++++++++++++++++++++++++++++")

    else:
        OPTION_FLAG = 0
        print("Exiting the whitecliffe Food Ordering system...")
        os._exit(0)  # This will exit the program
