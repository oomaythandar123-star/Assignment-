# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 21:47:47 2026

@author: Double-Y
"""

class product:
    def display(self):
        print("Welcome to Online Shopping!")

class clothes(product):
    def display(self):
        print("Product: Clothes")
        print("Price: 25000 MMK")

class electronics(product):
    def display(self):
        print("Product: Electronics")
        print("Price: 150000 MMK")

class food(product):
    def display(self):
        print("Product: Food")
        print("Price: 10000 MMK")

class shoes(product):
    def display(self):
        print("Product: Shoes")
        print("Price: 45000 MMK")

class accessories(product):
    def display(self):
        print("Product: Accessories")
        print("Price: 15000 MMK")


Product = product()
Clothes = clothes()
Electronics = electronics()
Food = food()
Shoes = shoes()
Accessories = accessories()


Product.display()
Clothes.display()
Electronics.display()
Food.display()
Shoes.display()
Accessories.display()