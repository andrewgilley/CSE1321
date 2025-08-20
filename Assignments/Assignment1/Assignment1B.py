# Class: CSE 1321L
# Section: W01
# Term: Fall Semester 2025 
# Instructor: Venkata Palagundla 
# Name: Andrew Gilley
# Assignment: #1

CONVERSION_FACTOR = 1000

print("[Electrical Energy Consumption Calculator]") 

volts = float(input("Enter the voltage (in volts): ")) 
ohms = float(input("Enter the resistance (in ohms): ")) 
hours = float(input("Enter the time the device was used (in hours): "))

temp_1 = (volts ** 2) * hours
temp_2 = ohms * CONVERSION_FACTOR

energy = temp_1 / temp_2
result = round(energy, 2)

print("The device consumed ", end = str(result))
print(" kWh of energy.")
