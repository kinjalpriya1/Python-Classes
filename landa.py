# def square(n):
#     return n**2

# x = square(10)

# lambda n:n**2
# x = f(20)


# ls = [1,2,3,4,5,10]
# sq = []

# for x in ls:
#     sq.append(square(x))
# print(sq)

# #map
# sq = list(map(square, ls))
# print(sq)


# def cube(n):
#     return n**3
#lambda n:n**3

ls = [1,2,3,4,5]
cubes = []

# for i in range(len(ls)):
#     cubes.append(cube(ls[i]))
cubes = list(map(lambda n:n**3, [1,2,3,4,5]))

print(cubes)



far = list(map(lambda c:c*(9/5) + 32, [1,10,50,100]))
print(far)





def filterEven(n):
    return n%2 == 0

ls = [1,2,3,4,5,6,7,8,9,10]

evens = []
for x in ls:
    if filterEven(x):
        evens.append(x)
print(evens)


evens = list(filter(lambda n: n%2==0, ls))
print(evens)




"""Lambda assignments"""

#1. 
def multiplyAll(*args):
    result = 0
    for i in args:
        result *= i
    print(result)

#2. 
def formatting(**kwargs):
    pass

#3. 
nums = [1,2,3,4,5,6]
strings = []
#strings = list(map(lambda n:"n", nums))
strings = list(map(lambda n:str(n), nums))
print(strings)

#4. 
nums = [1,3,5,8,15,20,30,40,50,60,70,80,90]
filteredNums = []
filteredNums = list(filter(lambda n: n % 3 == 0 and n % 5 == 0, nums))
print(filteredNums)

#5. 
nums = [1,3,5,8,15,20,30,40,50,60,70,80,90,100,140]
filteredNums = filter(lambda n: n > 50, nums)
list = list(map(lambda n: n*2, filteredNums))
print(list)