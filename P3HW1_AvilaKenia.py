
mod1 = float(input("enter grade for Module 1: "))
mod2 = float(input("enter grade for Module 2: "))
mod3 = float(input("enter grade for Module 3: "))
mod4 = float(input("enter grade for Module 4: "))
mod5 = float(input("enter grade for Module 5: "))
mod6 = float(input("enter grade for Module 6: "))
gradeList = [mod1,mod2,mod3,mod4,mod5,mod6]
lowest = min(gradeList)
highest = max (gradeList)
total = sum (gradeList)
avg = sum (gradeList)/len(gradeList)
#display results
print("\n------------results------------")
print(f'{"Lowest Grade:":<20}{lowest}')
print(f'{"Highest Grade:":<20}{highest}')
print(f'{"Sum of Grade:":<20}{total}')
print(f'{"Average:":<20}{avg:.2f}')
print("----------------------------")
# Detrmine letter grade based off the average
if avg>=90:
 
letter_grade ="A"
elif avg>=80:
 
letter_grade = "B"
elif avg>=70:
 
letter_grade = "C"
elif avg>=60:
 
letter_grade = "D"
elif avg<=59:
 
letter_grade = "F"
print(f"Average: {avg} 
Letter Grade: {letter_grade}")
