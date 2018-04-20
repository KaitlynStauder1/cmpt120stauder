# RobotStore.py
# Intro to Programming
# Author: Kaitlyn Stauder
# Date: April 16, 2018

from product import Product

def createProducts():
    productNames = ["Ultrasonic range finder",
                    "Servo motor",
                    "Servo controller",
                    "Microcontroller Board",
                    "Laser range finder",
                    "Lithium polymer battery"]
    productPrices = [2.50, 14.99, 44.95, 34.95, 149.99, 8.99]
    productQuantities = [4, 10, 5, 7, 2, 8]
    products = []
    total = ''
    for i in range(6):
        products.append(Product(productNames[i], productPrices[i], productQuantities[i]))
    return products

def printStock(products):
    print()
    print("Available Products")
    print("------------------")
    for i in range(0,len(products)):
        if products[i].getQuantity() > 0:
            products[i].getItems(i)
    print()
    
def main():
    products = createProducts()
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock(products)        
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
        if vals[0] == "quit":
            break
        prodId = int(vals[0])
        count = int(vals[1])
        if products[prodId].getInventory(count):
            if cash >= products[prodId].getCost(count):
                if products[prodId].getPurchase(count, cash):
                    cash -= products[prodId].getCost(count)
                    total = products[prodId].getTotal(count)
                    print("You have $", "{0:0.2f}".format(cash), "remaining.")
                else:
                    print("Sorry, you are unable to purchase the product.")
            else:
                print("Sorry, you cannot afford the product.")
        else:
            print("Sorry, there are only", products[prodId].getQuantity(), "left in stock.")
main()
