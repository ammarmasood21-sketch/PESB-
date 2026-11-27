# Beginner To-Do List Manager using a list of dictionaries and CRUD operations.

tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Enter task: ")

        if title == "":
            print("Task can't be empty")
        else:
            task = {"title": title, "done": False}
            tasks.append(task)
            print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet")
        else:
            for index in range(len(tasks)):
                if tasks[index]["done"] == True:
                    status = "[x]"
                else:
                    status = "[ ]"

                print(f"{index + 1}. {status} {tasks[index]['title']}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks yet")
        else:
            for index in range(len(tasks)):
                if tasks[index]["done"] == True:
                    status = "[x]"
                else:
                    status = "[ ]"

                print(f"{index + 1}. {status} {tasks[index]['title']}")

            task_number = int(input("Task number: "))

            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["done"] = True
                print("Marked as done:", tasks[task_number - 1]["title"])
            else:
                print("Invalid task number")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks yet")
        else:
            for index in range(len(tasks)):
                if tasks[index]["done"] == True:
                    status = "[x]"
                else:
                    status = "[ ]"

                print(f"{index + 1}. {status} {tasks[index]['title']}")

            task_number = int(input("Task number: "))

            if 1 <= task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                print("Deleted:", deleted_task["title"])
            else:
                print("Invalid task number")

    elif choice == "5":
        done_count = 0
        pending_count = 0

        for task in tasks:
            if task["done"] == True:
                done_count += 1
            else:
                pending_count += 1

        print("Done:", done_count, " Pending:", pending_count)
        print("Goodbye!")
        break

    else:
        print("Invalid option")
