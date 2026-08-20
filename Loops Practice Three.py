#Armstrong Numbers
num = int(input("Enter a number: "))
length = 0
ogNum = num

while num > 0:
    num = num // 10
    length += 1

num = ogNum
sum = 0

while num > 0:
    dig = num % 10
    sum += dig ** length
    num = num // 10

if sum == ogNum:
    print(f"{ogNum} is an Armstrong number")
else:
    print(f"{ogNum} is not an Armstrong number")


#2D List 

l1  =  [
#    0 1 2
    [1,2,35],   #0
    [3,4,5],   #1
    [8,6,2]    #2
    ]
l2 =  [
#    0 1 2
    [11,29,35],   #0
    [32,40,5],   #1
    [85,61,20]    #2
    ]

l3 = []
n = len(l1)
for i in range (n):
      l3.append([])

for i in range (len(l1)):
    for j in range (len(l1[i])):
          sum = l1[i][j] + l2[i][j]
          #print(f"l1[i][j] + l2[i][j]} = {sum}")
          l3[i].append(sum)

for i in range (len(l3)):
      for j in range (len(l3[i])):
            print(f"{l3[i][j]}")


#Print Patterns

#0. 
n = int(input("Input: "))

for i in range (n):
    for j in range (n):
        print("*", end=" ")
    print()

#1. 
n = int(input("Input: "))

for i in range (n + 1):
        print("*" * i)

#2.
n = int(input("Input: "))
num = 1

for i in range (1, n + 1):
    for j in range (i):
        print(num, end=" ")
        num += 1
    print()

#3.
n = int(input("Input: "))

for i in range (n, 0, -1):
    for j in range (1, i + 1):
        print(j, end=" ")
    print()