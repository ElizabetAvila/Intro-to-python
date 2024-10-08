#using python built- in librares

#importthedatetime library to use it in the program
import datetime

#assign the current date and time to a variable
time = datetime.datetime.now()
month = time.month



#Display date/time
print(f"The current date and time is {time}")
print(f"The currrent month is {month}")

today = datetime.datetime.today()
print(f"Today is {today}")

weekday = today.weekday()
weekday = int(weekday)
print(f"The day of the week is {weekday}\n")

print(type(weekday))
print()
'''
#Get day a week from user as integer
weekday = int(input("Enter an integer 0-6as the day of the week: "))
'''

# If-else statements determine the day of the week
if weekday == 0:
     weekday_word = "Monday"

if weekday ==1:
    weekday_word = "Tuesday"

if weekday == 2:
    weekday_word = "Wednesday"

if weekday == 3:
    weekday_word = "Thursday"

if weekday == 4:
    weekday_word = "Friday"

if weekday == 5:
    weekday_word = "Saturday"

if weekday == 6:
    weekday_word="Sunday"

else: print("inavlid day of the week !!!")
print()
print(f" The day of the week is {weekday_word}")
