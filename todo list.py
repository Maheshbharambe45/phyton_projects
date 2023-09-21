import json
import os

TODO_FILE = "todo.json"

def load_todo():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    else:
        return []

def save_todo(todo_list):
    with open(TODO_FILE, "w") as file:
        json.dump(todo_list, file)

def display_todo():
    todo_list = load_todo()
    if not todo_list:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task(task):
    todo_list = load_todo()
    todo_list.append(task)
    save_todo(todo_list)
    print("Task added successfully.")

def remove_task(index):
    todo_list = load_todo()
    if index < 1 or index > len(todo_list):
        print("Invalid task index.")
        return

    removed_task = todo_list.pop(index - 1)
    save_todo(todo_list)
    print(f"Removed task: {removed_task}")

def main():
    while True:
        print("=== To-Do List Application ===")
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_todo()
        elif choice == "2":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "3":
            display_todo()
            index = int(input("Enter the task number to remove: "))
            remove_task(index)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
