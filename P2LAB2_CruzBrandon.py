#Brandon R. Cruz
#20 June 2025
#P2LAB2 Aotomobile MPG Calculation
#The program allows the user to select a vehicle from a list and calculates how many gallons of fuel are needed to drive a number of miles.




vehicles = {'Camaro': 18.21, 'Prius': 52.36, 'Model S': 110, 'Silverado': 26}

keys = vehicles.keys()

print(keys)
print()
car_model = input("Enter a vehicle to see its mpg:11 ").capitalize()
print()
print(f"The {car_model} gets {vehicles[car_model]} mpg.")
print()
miles = float(input(f"How many miles will you drive the {car_model}? "))
gallons = miles / vehicles[car_model]
print()
print(f"{gallons:.2f} gallon(s) of gas are needed to drive the {car_model} {miles} miles.")
