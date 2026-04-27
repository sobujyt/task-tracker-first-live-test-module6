import sys

# Main task list - sob task ekhane thakbe
tasks = []

def display_menu() :
    print("\n===== Task Tracker =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Update Task Priority") # Notun priority option
    print("5. Exit")

def add_task() :
    title = input("Enter title: ")
    description = input("Enter description: ")
    
    # Priority input nebo user-er kach theke
    print("Choose Priority: High, Medium, Low")
    priority = input("Enter priority: ").capitalize()
    
    # Jodi user vul kichu likhe, tahole default Medium set hobe
    if priority not in ["High", "Medium", "Low"]:
        priority = "Medium"

    # Task dictionary te priority field add kora hoyeche
    task = {
        "title" : title,
        "description" : description,
        "priority" : priority
    }
    tasks.append(task)
    print("Task added successfully!")

def view_tasks() :
    if not tasks :
        print("\nNo tasks to show.")
        return
    
    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1) :
        # Output format onujayi task list dekhano hoyeche
        print(f"{index}. {task['title']} - {task['description']} [{task['priority']} Priority]")

def delete_task() :
    view_tasks()
    if tasks :
        try :
            task_num = int(input("Enter task number to delete : "))
            if 1 <= task_num <= len(tasks):
                tasks.pop(task_num - 1)
                print("Task deleted!")
            else :
                print("Invalid task number.")
        except ValueError :
            print("Please enter a valid number.")

def update_priority() :
    view_tasks()
    if not tasks :
        return
    
    try:
        task_num = int(input("Enter task number to update priority: "))
        if 1 <= task_num <= len(tasks) :
            # Notun priority value input neoya hobe
            new_priority = input("Enter new priority (High/Medium/Low): ").capitalize()
            
            if new_priority in ["High", "Medium", "Low"] :
                # Specific oi task-er priority update kora hobe
                tasks[task_num - 1]["priority"] = new_priority
                print("Task priority updated successfully!")
            else :
                print("Invalid priority! Use High, Medium, or Low.")
        else :
            print("Invalid task number.")
    except ValueError :
        print("Please enter a valid number.")

def main() :
    while True :
        display_menu()
        choice = input("Enter choice : ")

        if choice == '1' :
            add_task()
        elif choice == '2' :
            view_tasks()
        elif choice == '3' :
            delete_task()
        elif choice == '4' :
            update_priority() # Priority update function call kora holo
        elif choice == '5' :
            print("Exiting... Goodbye!")
            sys.exit()
        else :
            print("Invalid choice, please try again.")

if __name__ == "__main__" :
    main()
