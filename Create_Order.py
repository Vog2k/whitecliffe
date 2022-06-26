# Copyright 2022 by Nidhi Gowdra.
# All rights reserved.
# This file is part of the Whitecliffe Food Ordering System,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

class Create_Order(object):
    OrderNo = 1000  # Ticket number displayed starts from 2000
    """Class to create orders"""

    def __init__(self, ID, Name, Desc):
        self.ID = ID  # ID made up of the first characters of both first and last name plus the hexadecimal
        self.Name = Name  # Users name
        self.Desc = Desc  # User will enter problem and send a request
        self.OrderNo += 1
        Create_Order.OrderNo += 1
        self.Order_STATUS = "Open"
        self.Response = "N/A"
        # body of the constructor

    def Stats(Order_LIST):
        created = 0  # This will show the amount of tickets created finished and remaining being 0 until a ticket is
        # done
        finished = 0
        remaining = 0
        for obj in Order_LIST:
            created += 1
            if obj.Order_STATUS == "Closed" or obj.Order_STATUS == "Reopened":
                finished += 1
            else:
                remaining += 1
        return created, finished, remaining  # Once this ticket has been created it will add one to the following
