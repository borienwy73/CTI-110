#Brandon R. Cruz
#12 July 2025
#P5LAB
#This program simulates a self checkout system that calculates and breaks down the change owed to a customer into dollars and coins. 


import random

def disperse_change(amount):
    total_cents = int(amount * 100)

    dollars = total_cents // 100
    cents = total_cents - (dollars * 100)

    quarters = cents // 25
    cents = cents - (quarters * 25)

    dimes = cents // 10
    cents = cents - (dimes * 10)

    nickels = cents // 5
    cents = cents - (nickels * 5)

    pennies = cents

    if dollars == 1:
        print("1 Dollar")
    elif dollars > 1:
        print(f"{dollars} Dollars")

    if quarters == 1:
        print("1 Quarter")
    elif quarters > 1:
        print(f"{quarters} Quarters")

    if dimes == 1:
        print("1 Dime")
    elif dimes > 1:
        print(f"{dimes} Dimes")

    if nickels == 1:
        print("1 Nickel")
    elif nickels > 1:
        print(f"{nickels} Nickels")

    if pennies == 1:
        print("1 Pennie")
    elif pennies > 1:
        print(f"{pennies} Pennies")

    if total_cents == 0:
        print("No change")

# Define the main function
def main():
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${amount_owed}")

    amount_given = float(input("How much cash will you put in the self-checkout? "))

    change = round(amount_given - amount_owed, 2)

    print(f"Change is: ${change}")
    print()
    disperse_change(change)


# Call the main function
main()
