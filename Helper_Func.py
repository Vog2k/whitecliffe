# Copyright 2022 by Nidhi Gowdra.
# All rights reserved.
# This file is part of the Whitecliffe Food Ordering System,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

import datetime


class Helper_Func(object):
    """Class to make the system more readable"""

    def __init__():
        pass

    def DisplayOrder(obj):
        print("*******************")
        print("Order No: ", obj.OrderNo)
        print("ID: ", obj.ID)
        print("Name: ", obj.Name)
        print("Description of the issue: ", obj.Desc)
        print("Order Status: ", obj.Order_STATUS)

        if obj.Response != "N/A":
            print("Response: ", obj.Response)
        print("*******************")

    def UniqueToken(Order):
        timestamp = datetime.datetime.now()
        timestamp_req = str(timestamp.day + timestamp.month + timestamp.year)
        timestamp_req = int(timestamp_req[0:3])
        OrderNo_req = int(Order.OrderNo)  # Creates a hexadecimal password with two of the characters in the users name
        HEX_Token = Order.ID[0:2] + hex(OrderNo_req) + hex(timestamp_req)
        Order.Response = "Your unique token is: " + HEX_Token

        if Order.Order_STATUS == "Closed":
            Order.Order_STATUS = "Reopened"
        elif Order.Order_STATUS == "Open":  # Displays while finishing a ticket
            Order.Order_STATUS = "Closed"

        return Order

    def Menu():
        print("==============================================================")
        print("Select an option from the list below and press enter...")
        print("0. Exit")
        print("1. Create an order")
        print("2. Display orders")  # Main menu allowing 6 options
        print("3. Respond to an existing order")
        print("4. Reopen to an existing order")
        print("5. Display order stats")
        print("==============================================================")
        option = int(input("Enter the option number here: "))  # User input their number in this line
        return option
