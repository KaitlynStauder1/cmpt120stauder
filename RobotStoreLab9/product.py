#product.py
# Intro to Programming
# Author: Kaitlyn Stauder
# Date: April 16 2018

class Product:
        
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price
    
    def getQuantity(self):
        return self.quantity

    def getCost(self, quantity):
        return quantity * self.price

    def getInventory(self, quantity):
        return quantity <= self.quantity

    def getPurchase(self, quantity, money):
        if self.getInventory(quantity) and self.getCost(quantity) <= money:
            self.quantity = self.quantity - quantity
            print("You purchased", quantity, self.name + '(s).')
            return True
        else:
            print("Sorry we are sold out of", self.name)
            return False

    def getItems(self, number):
        print(str(number) + ')', self.quantity, self.name + 's', '$', '{:.2f}'.format(self.price))

    def getTotal(self, quantity):
        total = str(quantity * self.price)
        print("The total comes to $", total)
