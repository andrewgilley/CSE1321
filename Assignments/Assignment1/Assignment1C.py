# Class: CSE 1321L
# Section: W01
# Term: Fall Semester 2025 
# Instructor: Venkata Palagundla 
# Name: Andrew Gilley
# Assignment: #1

print("[Weight Conversion - Kilograms to Stones and Pounds]")

weight = float(input("Enter weight in kilograms: "))

stones = weight * 0.157473
stones_whole = int(stones)

decimal = stones - stones_whole
pounds = round(decimal * 14, 2)

print(str(weight) + " kilograms is approximately ", end = str(stones_whole))
print(" stones and", str(pounds) + " pounds.")
