#Brandon R. Cruz
#6 JULY 2025
#P4HW2
#The program calculates and displays the regular pay, overtime pay, and totalfor each employee enetered by the user.

#Start

#Set all totals to 0

#While the user doesn’t type "Done":
    #Ask for employee name
    #Ask for hours worked and pay rate
    #If hours > 40:
        #Calculate overtime
    #Else:
        #No overtime
    #Calculate total pay
    #Add to totals
    #Show employee pay info

#Show total employees and total pay




state = "Run"

num_emp = 0
total_overtime_pay = 0
total_regular_pay = 0
total_pay = 0

while state == "Run":
    name = input("Enter employee's name or 'Done' to terminate: ")
    
    if name == "Done":
        state = "Stop"
    else:
        hours = float(input(f"How many hours did {name} work? "))
        pay_rate = float(input(f"What is {name}'s pay rate? "))

        if hours > 40:
            over_time = hours - 40
            regular_pay = 40 * pay_rate
        else:
            over_time = 0
            regular_pay = hours * pay_rate

        over_time_pay = over_time * (1.5 * pay_rate)
        gross_pay = regular_pay + over_time_pay

        num_emp = num_emp + 1
        total_overtime_pay = total_overtime_pay + over_time_pay
        total_regular_pay = total_regular_pay + regular_pay
        total_pay = total_pay + gross_pay
            
        print()
        print(f"Employee name:   {name}")
        print()
        print(f"{'Hours Worked':<15}{'Pay Rate':<10}{'OverTime':<10}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<10}")
        print('-----------------------------------------------------------------------------------')
        print(f"{hours:<15}{pay_rate:<10}{over_time:<10}${over_time_pay:<15.2f}${regular_pay:<15.2f}${gross_pay:<10.2f}")
else:
    print()
    print(f"Total number of employees entered: {num_emp}")
    print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
    print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
    print(f"Total amount paid in gross: ${total_pay:.2f}")

