# Copyright 2022 by Nidhi Gowdra.
# All rights reserved.
# This file is part of the Whitecliffe Food Ordering System,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

class Create_Order(object):
    OrderNo = 1000
    """Class to create orders"""
    def __init__(self, ID, Name, Desc):
        self.ID = ID
        self.Name = Name
        self.Desc = Desc
        self.OrderNo += 1
        Create_Order.OrderNo += 1
        self.Order_STATUS = "Open" 
        self.Response = "N/A"

    def Stats(Order_LIST):
        created = 0
        finished = 0
        remaining = 0
        for obj in Order_LIST:
            created += 1
            if obj.Order_STATUS == "Closed" or obj.Order_STATUS == "Reopened":
                finished += 1
            else:
                remaining += 1
        return created, finished, remaining