# Kenia Avila
# 10/29/2024
# P3HW2
# Program calculates paycheck based on OT or no OT
name=input("enter employee's name: ")
hours=int(input("Enter number of hours worked: "))
pay_rate=float(input("Enter employee's pay rate: "))
print('-------' * 8)
print(f"employee name: {name}")
print()
print()
if hours > 40:
 
ot_hours= hours - 40
 
ot_pay_rate= 1.5*pay_rate
 
ot_pay_amount=ot_hours*ot_pay_rate
 
reg_hour_pay= 40*pay_rate
 
gross_pay= ot_pay_amount+reg_hour_pay
else: 
 
ot_hours=0
 
ot_pay_amount=0
 
reg_hour_pay=pay_rate * hours
 
gross_pay=(reg_hour_pay)
print(f"{'Hours Worked':<20}{'Pay Rate':<20}{'OverTime':<20}{'OverTime Pay':<20}{'RegHour Pay':<20}{'Gross Pay':<20}")
print('------' * 20)
print(f"{hours:<20}${pay_rate:<20.2f}{ot_hours:<20}{ot_pay_amount:<20.2f}{reg_hour_pay:<20.2f}{gross_pay:<20.2f}")
