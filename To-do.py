tasks = []

def addTask():
    title = input("What is the title: ")
    for task in tasks:
        if title == task["title"]:
            print("Tasks already exists")
            break
    else: 
        priority = input("What is the priority: ")
        status = False
        task = {
            "title": title,
            "priority": priority,
            "status": status
            }
        tasks.append(task)
        print("Task added succesfully")

def removeTask():
    taskTitle = input("Which task do you want to remove: ")
    for task in tasks:
            if taskTitle == task["title"]:
                 tasks.remove(task)
                 break
    else:
        print("Task not found")

def showTasks():
    if len(tasks) > 0: 
        for task in tasks:
            print(f"""
                {task["title"]}
                Priority: {task["priority"]}
                Status: {task["status"]}
            """)
    else: 
        print("No tasks available")

def modifyTask():
    existingTask = input("What is the title of the task you want to change: ")
    for task in tasks: 
        if existingTask == task["title"]:
            title = input("What is the title of the task: ")
            priority = input("What is the priority: ")
            status = False
            task = {
                "title": title,
                "priority": priority,
                "status": status
                    }
            tasks.append(task)
            print("Task added succesfully")
    else:
        print("Task not found")

def completeTask():
    title = input("What is the title of the task you want to change: ")
    for task in tasks: 
        if title == task["title"]:
                priority = priority
                status = True
                task = {
                    "title": title,
                    "priority": priority,
                    "status": status
                        }
                tasks.append(task)
                print("Task marked as complete")
    else:
        print("Task not found")

def exit():
    print("Goodbye!")
    


while True:
    print("""
---------------- TO-DO APP ----------------

1. Add Task
2. Remove Task
3. Show Tasks
4. Modify Task
5. Mark Task as Completed
6. Exit

--------------------------------------------
    """)
    choice = int(input("What do you want to do: "))
    if choice == 1:
        addTask()
    elif choice == 2:
        removeTask()
    elif choice == 3:
        showTasks()
    elif choice == 4: 
        modifyTask()
    elif choice == 5:
        completeTask()
    elif choice == 6:
        exit()
        break
    