
#Kenia Avila
#10/17/24
#P2HW1
#Assignment assess student ability to edit and enhance exiting programs
print("This program calculates amd displays travel expenses")
Budget = float(input("Enter Budget: "))
print()
Location = input("Enter your travel destination: ")
print()
Fuel = float(input("How much do you think you will spend on gas? "))
print()
Accomodation = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()
Food = float(input("Last, how much do you need for food? "))
Remaining = Budget - Fuel - Accomodation - Food
print("-*- " *9, "Travel Expenses", "-*-" *9)
print(f"{'Location:':<20}{Location}")
print(f"{'Initial Budget:':<20}${Budget:,.2f}")
print(f"{'Fuel:':<20}${Fuel:,.2f}")
print(f"{'Accomodation:':<20}${Accomodation:,.2f}")
print(f"{'fuel:':<20}${Fuel:,.2f}")
print(f"{'Food:':<20}${Food:,.2f}")
print("-*-" * 11)
print(f"{'Remaining Balance:':<20}${Remaining:,.2f}")
