#Kenia Avila
#11/14/24
#loop
numEmp=0
numOt=0
numHours=0
numGross=0
name=input("enter employee's name or 'done' to terminate: ")
while name!= "done":
 numEmp += 1
 hours=int(input(f"Enter number of hours {name} worked: "))

 pay_rate=float(input(f"Enter {name} pay rate: "))
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
 print(f"employee name: {name}")
 print(f"{'Hours Worked':<20}{'Pay Rate':<20}{'OverTime':<20}{'OverTime Pay':<20}{'RegHour Pay':<20}{'Gross Pay':<20}")
 print('------' * 20)
 print(f"{hours:<20}${pay_rate:<20.2f}{ot_hours:<20}{ot_pay_amount:<20.2f}{reg_hour_pay:<20.2f}{gross_pay:<20.2f}")
 print('-------' * 8)
 numOt +=ot_pay_amount
 numGross +=gross_pay
 numHours += reg_hour_pay

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
 name=input("enter employee's name or 'done' to terminate: ")

print(f"total number of employees entered : {numEmp}")
print(f"total amount paid for overtime: ${numOt:.2f}")
print(f"total amount paid for regular hours : ${numHours:.2f}")
print(f"totalamount paid in gross: ${numGross:.2f}")
