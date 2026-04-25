import sys

# surur list
tasks = []

def display_menu():
    print("\n===== Task Tracker =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

def add_task():
    title = input("Enter title: ")
    description = input("Enter description: ")

    task = {
        "title": title,
        "description": description,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("\nNo tasks to show.")
        return
    
    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        # status check korar jonno
        status = "[Completed]" if task["completed"] else "[Not Completed]"
        print(f"{index}. {task['title']} - {task['description']} {status}")

def delete_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                tasks.pop(task_num - 1)
                print("Task deleted!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def mark_completed():
    view_tasks()
    if not tasks:
        return
    
    try:
        task_num = int(input("Enter task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):

            tasks[task_num - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("Enter choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            mark_completed()
        elif choice == '5':
            print("Exiting... Goodbye!")
            sys.exit()
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
