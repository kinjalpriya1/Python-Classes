
# def add(a,b):
#     return a + b

# def subtract(a,b):
#     return a - b

# def multiply(a,b):
#     return a * b

# def divide(a,b):
#     return a / b

# def callChoice(choice,a, b):
#     if choice == 1:
#         adding = add(a,b)
#         print(adding)
#     elif choice == 2:
#         subing = subtract(a,b)
#         print(subing)
#     elif choice == 3:
#         multiplying = multiply(a,b)
#         print(multiplying)
#     elif choice == 4:
#         dividing = divide(a,b)
#         print(dividing)

# while True:
#     print("""
#         -Calculator-
#         1. add
#         2. subtract
#         3. multiply
#         4. divide
# """)
#     choice = int(input("Which task do you want to do: "))
#     a = int(input("What is the first number: "))
#     b = int(input("What is the second number: "))
#     callChoice(choice, a, b)

#2

def countdown(n):
    if n == 0:
        print("Blast Off!")
        return
    print(n)
    n -= 1
    countdown(n)  

n = int(input("Enter a number: "))
countdown(n)

#3

def fun(n):
    if n == 0:
        return
    print(n)
    #n -= 1
    fun(n - 1)
    fun(n - 1)


n = int(input("Enter a number: "))
fun(n)