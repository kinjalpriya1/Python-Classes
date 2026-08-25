import random
list = []

for i in range(100):
    list.append(random.randint(1,100))

print([x for x in list if x % 5 == 0 and x % 10 == 0])

names = ["Amelia","Alexander","Aria","Asher","Benjamin","Clara","Daniel","Elijah","Grace","Henry"]
print([f"{x} has even number of letters" for x in names if len(x) % 2 == 0])