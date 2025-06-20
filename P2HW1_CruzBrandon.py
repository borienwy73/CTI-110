#Brandon R. Cruz
#20 June 2025
#P2HW1 Budget with aligned columns
#This program calculates and displays estimated travel expenses based on user's input and after collecting inputs, it calculates the remaining balance. 



print("This program calculates and displays travel expenses")
print()
budget = float(input("Enter Budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gas = float(input("How much do you think you will spend on gas? "))
print()
accomodation = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food = float(input("Last, how much do you need for food? "))
print()

remaining_balance = budget - gas - accomodation - food

print("------------Travel Expenses------------")
print(f"{'Location:':<20} {destination}")
print(f"{'Initial Budget:':<20} ${budget:.2f}")
print(f"{'Fuel:':<20} ${gas:.2f}")
print(f"{'Accomodation:':<20} ${accomodation:.2f}")
print(f"{'Food:':<20} ${food:.2f}")
print("---------------------------------------")
print()
print(f"{'Remaining balance:':<20} ${remaining_balance:.2f}")




