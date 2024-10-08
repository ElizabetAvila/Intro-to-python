# Kenia Avila
# 10-8-24
#P2LAB1
#using python's built in math library

#import math libarary
import math

print(f"The value of pi is {math.pi}\n")

#Get radius from user
radius = float(input("what is the radius of the circle? "))
print()

#Calculate the diameter
diameter = 2 * radius


#Display diameter with one decimal place
print(f"The diameter of the circle is {diameter:.1f}\n")


#Calculate the circumference
circumf = 2 * math.pi * radius

#Display the circumference
print(f"The circumference of the circle is {circumf:.2f}\n")

#Calculate the area of the circle
area = math.pi * math.pow(radius,2)

#Display the area of the circle
print(f"The area of the circle is {area:.3f}\n")


