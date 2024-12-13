
#Kenia Avila
#11/12/24
#input grades with loop
#list possible grades
numGrades = int(input("How many scores do you want to enter? "))
for grades in range(numGrades):
 
thisGrade = int(input(f"Enter score #{grades + 1}: "))
 
#Loop to ensure thisGrade is in possiblGrades
 
while thisGrade <0 or thisGrade >100:
 
print(f"{thisGrade}INVALID!!!")
 
thisGrade = int(input(f"Enter score#{grades + 1} again: "))
 
#add the valid score
#loop to print each item in the cart
 
print()
 
print("Modified list: ")
 
print(thisGrade)
