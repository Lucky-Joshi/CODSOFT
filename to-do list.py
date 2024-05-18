import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#Function to display Menu of choices.
def display_menu():
    clear_screen()
    print("To-Do List Application")
    print("----------------------")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    print()

#Function to view To-Do List.
def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    input("\nPress Enter to continue...")

#Function to add tasks from To-Do List.
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"'{task}' has been added to your to-do list.")
    input("Press Enter to continue...")

#Function to remove tasks from To-Do List.
def remove_task(tasks):
    if not tasks:
        print("Your to-do list is empty.")
        input("Press Enter to continue...")
        return

    view_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"'{removed_task}' has been removed from your to-do list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    input("Press Enter to continue...")

#Main Function to be perform.
def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

main()1

