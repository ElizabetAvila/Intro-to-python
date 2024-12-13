
#kenia Avila
#10/3/24
#P1HW2
#create a program that does some basic math on numbers that are entered
#Get information for budjet
print("This program calculates and displays travel expenses")
Budjet = float(input("Enter Budjet: "))
print()
destination = input("Enter your travel destination: ")
print()
Gas = float(input( "How much do you think you will spend on gas?"))
print()
Accomidation = float(input("Approximately , how much will you need for accomodation/hotel?"))
print()
Food = float(input("Last, how much do you need for food?"))
print()
#Display at the top of the reciept
print("-" * 4, "Travel Expenses" ,"-" *4 )
print()
total= (Budjet - Gas - Accomidation - Food)
print(f"Location: {destination}")
print (f"Intial budjet: {Budjet :.2f}")
print()
print(f"Fuel: {Gas}")
print(f"Accomidation: {Accomidation}")
print(f"Food: {Food}")
print (f"Remaining Balnance: {total :.2f}")
