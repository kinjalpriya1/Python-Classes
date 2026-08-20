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

for i in range (len(l1)):
    for j in range (len()):
