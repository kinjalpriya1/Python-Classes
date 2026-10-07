import math

while True:
    print("""
        -Calculator-
        1. sine
        2. cosine
        3. tan
        4. cosecant
        5. secant
        6. cot
""")
    choice = int(input("Which task do you want to do: "))
    num = int(input("What is the input number: "))
    if choice == 1:
        print(math.sin(math.radians(num)))
    elif choice == 2:
        print(math.cos(math.radians(num)))
    elif choice == 3:
            print(math.tan(math.radians(num)))
    elif choice == 4:
            print(math.asin(math.radians(num)))
    elif choice == 5:
            print(math.acos(math.radians(num)))
    elif choice == 6:
            print(math.atan(math.radians(num)))