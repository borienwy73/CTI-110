
#Brandon R. Cruz
#16 JUNE 2025
#P1HW2 Assignment
#Program that calculates itemized expenses while calculating the remaining balance of an established budget.






#Pseudocode:
#Display a message indicating that the program calculates travel expenses.
#Prompt user to enter their total budget and store it.
#Prompt user to enetr their travel destination and store it.
#Prompt the user to enter estimated costs for:
#gas
#Accomodation/Hotel
#Food
#Calculate the remaining balance by substracting the total expenses(gas+accomodation).
#Display a formatted summarry of the travel expenses.
#Display the report with the remaining blance.




print(" This programs calculates and displays travel expenses")
print()
budget = int (input("Enter Budget:  "))
print()
destination=input ("Enetr your travel destination: ")
print()
gas = int(input("How much do you think you will spend on gas? "))
print()
accomodation = int(input("Approxiamately, how much will you need for accomodation/hotel? "))
print()
food= int(input("Last, how much do you need for food? "))
print()

remaining_balance =budget - gas - accomodation -food


print("------------Travel Expenses------------")
print("Location:" , destination)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accomodation:", accomodation)
print("Food:", food)
print()
print("remaining Balance:", remaining_balance)



