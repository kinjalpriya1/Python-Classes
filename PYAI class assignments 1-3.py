#Supermarket Discount

purchase = float(input("Total purchase amount: "))
userCode = input("Enter your coupon code: ")

if purchase > 500:
    discount = 0.05
    purchase = purchase - (purchase * discount)
if userCode == "SAVE10": 
    discount = 0.5
    purchase = purchase - (purchase * discount)

print(f"Final bill: {purchase}")

#Movie Ticket Booking

age = int(input("Enter age: "))
student = input("Yes/No: ")
price = 200

if age < 12:
    discount = 0.5
    price = price - (price * discount)
if student == "yes": 
    discount = 0.2
    price = price - (price * discount)

print(f"Final bill: {price}")

#Electricity Bill

units = int(input("Input units consumed: "))

if units <= 100:
    pricePerUnit = 5
elif units <= 300: 
    pricePerUnit = 7
else:
    pricePerUnit = 10

bill = units * pricePerUnit
if bill > 1500:
    surcharge = 0.08
    bill = bill + (bill * surcharge)

print(f"Final bill: {bill}")