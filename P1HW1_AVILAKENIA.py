#Kenia
#9/24/2024
#P1HW1
#get integer input from the user and preform math calculations

print("----Calculating Exponents----")
print()
print()
print()

# Get info from user
base_value = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))
print()
print()

#calculate the value of the exponent match
result = base_value  ** exponent

# Display results of the math
print(base_value, "raised to the power of", exponent, "is", result, "!!")
print()
print()
print("----Addition and Subtraction----")

#get some info from the user
start_int = int(input("Enter the starting integer: "))
add_int = int(input("Enter an integer to add: "))
sub_int = int(input("Enter an integer to subtract: "))
print()
print()
print()

#calculate the math
result2 = start_int + add_int - sub_int


#Display the Results2

print(start_int, "+", add_int, "-", sub_int,"is equal to", result2)

