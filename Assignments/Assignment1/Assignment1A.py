# Class: CSE 1321L
# Section: W01
# Term: Fall Semester 2025 
# Instructor: Venkata Palagundla 
# Name: Andrew Gilley
# Assignment: #1

print("[Customer Receipt Generator]")

name = input("Enter your name: ") 
item = input("Enter the item you purchased: ") 
quantity = input("Enter the quantity of the item: ") 

print("Thank you, ", end = name + "! ")
print("You ordered ", end = quantity + " " + item + "(s).")
