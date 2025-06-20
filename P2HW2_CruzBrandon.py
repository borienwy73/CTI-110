#Brandon R Cruz
#20 June 2025
#P2HW2 Module Assignment

-------PSEUDOCODE---------

START

Create empty list called grades

FOR module_number FROM 1 TO 6 DO:
    PROMPT user to enter grade for Module module_number
    CONVERT input to number
    ADD grade to grades list

SER lowest_grade TO minumum value in grades
SET highest_grades TO maximum value in grades
SET sum_grades TO total of all grades
SET average_grades TO sum_grades divided by number of grades


DISPLAY-------------Results----------------

DISPLAY "Lowest Grade:" and lowest_grade
DISPLAY "Highest Grade:" and highest_grade
DISPLAY "Sum of Grades:" and sum_grades
DISPLAY "Average:" and average_grade rounded to 2 decimal places
DISPLAY "-------------------------------------------"


END



grades = []

grade1 = float(input("Enter grade for Module 1: "))
grades.append(grade1)
grade2 = float(input("Enter grade for Module 2: "))
grades.append(grade2)
grade3 = float(input("Enter grade for Module 3: "))
grades.append(grade3)
grade4 = float(input("Enter grade for Module 4: "))
grades.append(grade4)
grade5 = float(input("Enter grade for Module 5: "))
grades.append(grade5)
grade6 = float(input("Enter grade for Module 6: "))
grades.append(grade6)

lowest_grade = min(grades)
highest_grade = max(grades)
sum_grades = sum(grades)
average_grade = sum_grades / len(grades)

print()
print("------------Results------------")
print(f"{'Lowest Grade:':<20}{lowest_grade}")
print(f"{'Highest Grade:':<20}{highest_grade}")
print(f"{'Sum of Grades:':<20}{sum_grades}")
print(f"{'Average:':<20}{average_grade:.2f}")
print("-----------------------------------------")





