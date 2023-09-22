#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
print("Welcome to the tip calculator!")
bill =(input("What was the total bill? $"))
tip= float(input("How much tip would you like to give? 10,12 or 15? "))
bill = (float(bill))
tip = (tip/100)
persent = (bill*tip)
people = (input("How many people to split the bill? "))
people = (float(people))
spent = (persent+bill)
final_amount= (round(spent/people,2))


# FAQ: How to round to 2 decimal places?

# Find the answer in the Q&A here: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048


print(f"Each person should pay: ${final_amount}")