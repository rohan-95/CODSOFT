tasks = []

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f'Task "{task}" added to the to-do list.')

def view_tasks():
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def complete_task():
    if not tasks:
        print("No tasks in the to-do list.")
        return

    task_index = int(input("Enter the index of the task to complete: "))
    if 1 <= task_index <= len(tasks):
        completed_task = tasks.pop(task_index - 1)
        print(f'Task "{completed_task}" marked as completed.')
    else:
        print("Invalid task index. Please enter a valid index.")

while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        complete_task()
    elif choice == '4':
        print("Exiting from to-do list program. Thank You for using Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4).")
