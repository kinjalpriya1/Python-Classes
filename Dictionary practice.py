#1
student = {
    "name": "Rahul",
    "age": 14,
    "school": "ABC School"
}

print(student["name"])
print(student["age"])
print(student["school"])

#2
student["school"] = "Hogwarts"
student["city"] = "Toronto"
print(student)

#3
employee = {
    "name": "Akash",
    "department": "IT",
    "salary": 50000,
    "city": "Bengaluru"
}

print(employee.keys())
for key in employee.keys():
    print(key)

print(employee.values())
for values in employee.values():
    print(values)

print(employee.items())
for items in employee.items():
    print(items)

#4
product = {
    "name": "Laptop",
    "price": 65000,
    "brand": "Dell",
    "stock": 15
}

print(product["name"])
print(product["price"])
print(product["brand"])
product["stock"] = 20
product["colour"] = "Silver"
print(product)

#5.
weather = {
    "city": "Mumbai",
    "main": {
        "temperature": 31,
        "humidity": 78
    },
    "wind": {
        "speed": 12
    }
}

print(weather["city"])
print(weather["main"]["temperature"])
print(weather["main"]["humidity"])
print(weather["wind"]["speed"])

#6
student = {
    "name": "Hanish",
    "age": 13,
    "marks": 89,
    "address": {
        "city": "Delhi",
        "state": "Delhi"
    }
}

print(student["name"])
print(student["marks"])
print(student["address"]["city"])
student["course"] = "Python"
student["marks"] = 95
for items in student.items():
    print(items)