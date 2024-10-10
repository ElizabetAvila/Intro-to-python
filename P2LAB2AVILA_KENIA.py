#Kenia Avila
#10/10/24
#P2LAB2
#program that creates a dictionary where the key and value pairs are as follows.

#Create a dictionary
cars = {"Camaro" :18.21, "Prius" :52.36, "Model S" :110,"Silverado" : 26}

# Variable that hold only key from dictionary
keys = cars.keys()

#show all the keys to the user
print(keys)

# Get a car (key) from the user
selected_car = input("Enter a vehicle to see it's mpg:")

# Display the selected car and it's mpg
print(f"The {selected_car} gets {cars[selected_car]} mpg.")
print()

#Get the nnumber of miles to drive the car
miles_planned = float(input(f" how many miled will you drive  the {selected_car}?"))
# Calcukate gallons of gas needed
gas_needed = miles_planned / cars[selected_car]

#Display gallons needed to user
print(f"{gas_needed:.2f} gallon(s)of gas are needed to drive the {selected_car} {miles_planned} miles.")
