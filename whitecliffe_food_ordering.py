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

print("Welcome to the whitecliffe Food Ordering system")

while OPTION_FLAG != 0:
    option = Helper_Func.Menu()

    if option == 1:
        while(CREATE_FLAG == 1):
            print("Please input Staff Name and press enter")
            ID = input()
            print("Please input the description of the order/s and press enter")
            print("[If you require a unique order token, input UOT and press enter]")
            Order_Desc = input()
            print("Please input your Name (optional) and press enter")
            Name = input()

            if Name == "":
                Name = "Not specified"

            Order = Create_Order(ID, Name, Order_Desc)           

            if "UOT" in Order.Desc:
                Order = Helper_Func.UniqueToken(Order)
                Helper_Func.DisplayOrder(Order)
                Order_LIST.append(Order)
            else:
                Order_LIST.append(Order)

            print("Do you want to create another order? (Y/N)")
            user_in = input()
            if user_in == "N" or user_in == "n":
                CREATE_FLAG = 0

    elif option == 2:
        for obj in Order_LIST:
            print("*******************")
            print("Order No: ", obj.OrderNo)
            print("ID: ", obj.ID)
            print("Name: ", obj.Name)
            print("Description of the order: ", obj.Desc)
            print("Order Status: ", obj.Order_STATUS)

            if obj.Response != "N/A":
                print("Response: ", obj.Response)
            print("*******************")

    elif option == 3:
        print("Please enter the Order number to respond: ")
        USER_IN_Order_NO = int(input())

        for obj in Order_LIST:
            if obj.OrderNo == USER_IN_Order_NO:
                print("Please enter the response for the Order No: ", obj.OrderNo)
                RESPONSE_INPUT = input()
                obj.Response = RESPONSE_INPUT
                obj.Order_STATUS = "Closed"              

    elif option == 4:
        print("Please enter the Order number to reopen: ")
        USER_IN_Order_NO = int(input())

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
        print("Finished: ", F)
        print("Remaining: ", R)
        print("++++++++++++++++++++++++++++")

    else:
        OPTION_FLAG = 0
        print("Exiting the whitecliffe Food Ordering system...")
        os._exit(0)