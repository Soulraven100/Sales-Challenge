name = input("What is your full name? ")
sales = float(input("How much have you sold this month in $? "))
commission_percent = .13
commision = sales * commission_percent
commision2 = (round(commision, 2))
print(f"{name} your commision this month is ${commision2}. Good Work!" )