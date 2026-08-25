

list = []

while True:
    print("""
    ---------To Do's---------
    1. Add Task
    2. Remove Task
    3. Modify Task
    4. Show Tasks
    5. Exit
""")
    choice = int(input("What do you want to do: "))
    if choice == 1:
        task = input("What do you want to add: ")
        if task in list:
            print("Task exists already in the list")
        else:
            list.append(task)
            print("Task added")
    elif choice == 2:
        task = input("What do you want to remove: ")
        if task in list:
            list.remove(task)
            print("Task removed")
        else:
            print("Task does not exist")
    elif choice == 3:
        task = input("Which task do you want to change: ")
        if task in list:
            index = list.index(task)
            new = input("What's the new task: ")
            list[index] = new
            print("Task changed")
        else:
            print("Task does not exist")
    elif choice == 4:
        for i, element in enumerate(list, 1):
            print(f"{i}. {element}")


