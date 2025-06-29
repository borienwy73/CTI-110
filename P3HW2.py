name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

if hours > 40:
    over_time = hours - 40
    regular_pay = 40 * pay_rate
else:
    over_time = 0
    regular_pay = hours * pay_rate

over_time_pay = over_time * (1.5 * pay_rate)

gross_pay = regular_pay + over_time_pay

print("----------------------------------")
print(f"Employee name:   {name}")
print(f"{'Hours Worked':<15}{'Pay Rate':<10}{'OverTime':<10}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<10}")
print('-----------------------------------------------------------------------------------')
print(f"{hours:<15}{pay_rate:<10}{over_time:<10}${over_time_pay:<15.2f}${regular_pay:<15.2f}${gross_pay:<10.2f}")
