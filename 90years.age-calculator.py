age = input("What is your current age? ")
age = int(age)
days= (age*365)
days= (90*365)-days
week = (age*52)
week=(90*52)-week
month = (age*12 )
month = (90*12)-month
result = (f"You have {days} days, {week} weeks, and {month} months left.")
print(result)
