#Brandon R. Cruz
#6 JULY 2025
#P4HW1
#Program collects a number of test scores, calculates averages, removes the lowest grade and then assigns a letetr grade.


#-------PSEUDOCODE---------
#Start


#Ask how many scores:
#Repeat for each score:
      #Get score
      #If score is invalid, ask again
      #Add score to list


#remove the lowest score

#Calculate average of ramaining scores

#Find letter grade from average

#Show lowest score, new list, average, and grade

#End





grades = []

number_of_scores = int(input("How many scores do you want to enter? "))

for i in range(number_of_scores):
    score = float(input(f"Enter score #{i+1}: "))
    
    while score < 0 or score > 100:
        print()
        print("INVALID score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{i+1} again: "))
    grades.append(score)

lowest_grade = min(grades)
grades.remove(lowest_grade)

sum_grades = sum(grades)
average_grade = sum_grades / len(grades)

if average_grade >= 90:
    grade = "A"
elif average_grade >= 80:
    grade = "B"
elif average_grade >= 70:
    grade = "C"
elif average_grade >= 60:
    grade = "D"
else:
    grade = "F"

print()
print("------------Results------------")
print(f"{'Lowest Score':<15}: {lowest_grade}")
print(f"{'Modified List':<15}: {grades}")
print(f"{'Scores Average':<15}: {average_grade:.2f}")
print(f"{'Grade':<15}: {grade}")
print("-----------------------------------------")





