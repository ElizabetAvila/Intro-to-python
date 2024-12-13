
#KeniaAvila
#11/10/24
#Write a program that asks the user to enter an integer and dsiplay multiplication table
def display_multiplication_table(number):
 
for integer in range(1, 13):
 
print(f"{number} x {integer} = {number * integer}")
def main():
 
while True:
 
try:
 
user_input = int(input("Enter an integer: "))
 
except ValueError:
 
print("Please enter a valid integer.")
 
continue
 
 
if user_input < 0:
 
print("This program does not handle a negative number.")
 
else:
 
display_multiplication_table(user_input)
 
 
run_again = input("Would you like to run the program again? ").lower()
 
 
if run_again = "yes":
 
print("Goodbye!")
 
break
if __name__ == "__main__":
 
main()
