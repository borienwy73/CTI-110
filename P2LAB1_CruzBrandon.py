#Brandon R. Cruz
#20 June 2025
#P2LAB1 Circle Formulas
#This program calculates and displays the diameter, circumference, and area of a circle based on a raduius eneterd by the user.



pi = 3.14159

radius = float(input("What is the radius of the circle? "))

diameter = radius * 2
circumference = 2 * pi * radius
area = pi * (radius ** 2)

print()
print(f"The diameter of the circle is {diameter:.1f}")
print()
print(f"The circumference of the circle is  {circumference:.2f}")
print()
print(f"The area of the circle is {area:.3f}")

