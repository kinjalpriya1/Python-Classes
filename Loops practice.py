# 1. Prime Factorization

# n = int(input("Enter a number: "))
# prime = "no"

# for i in range(2,n - 1):
#     if n % i == 0:
#         prime = "yes"

# if prime == "no":
#     print(f"{n} is a prime number")

#Counting letters

# name = input("Enter name: ")
# countedChars = []
# count = 0

# for x in name:
#     #name.count(x)
#     if x in countedChars:
#         continue
#     countedChars.append(x)
#     #print()
#     for y in name:
#         if y == x:
#             count += 1

#5. Sum of Digits

# num = int(input("Enter a multi-digit number: "))
# sum = 0

# while num > 0:
#     digit = num % 10
#     sum = sum + digit
#     num = num // 10

# print(sum) 

#6. Sum of Squares of Digits

# num = int(input("Enter a multi-digit number: "))
# sum = 0

# while num > 0:
#     digit = num % 10
#     sum = sum + (digit ** 2)
#     num = num // 10

# print(sum) 

#7. Count Even and Odd Digits

# num = int(input("Enter a multi-digit number: "))
# even = []
# odd = []

# while num > 0:
#     digit = num % 10
#     if digit % 2 == 0:
#         even.append(digit)
#     else:
#         odd.append(digit)
#     num = num // 10

# print(f"""Even digits: {len(even)} ({even})
# Odd digits: {len(odd)} ({odd})""") 

#8. Reverse a Number

# list = []
# num = int(input("Enter a multi-digit number: "))
# while num > 0:
#     digit = num % 10
#     list.append(digit)
#     num = num // 10
# print(list[::1], sep="")

#9. 

list = []
num = int(input("Enter a multi-digit number: "))
while num > 0:
    digit = num % 10
    list.append(digit)
    num = num // 10
if list[::1] == list[::-1]:
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")