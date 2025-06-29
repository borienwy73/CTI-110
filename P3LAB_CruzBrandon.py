#Brandon R. Cruz
#29 JUNE 2025
#P3LAB Coin Change
#Program calculates number of dollars and coins given an amount of money.





amount = float(input("Enter the amount of money as a float: $"))

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


