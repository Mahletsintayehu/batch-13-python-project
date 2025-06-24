# 3. To-Do List App (Text-Based)
# Build a to-do list manager that:
# Allows users to add tasks with priorities (e.g., "Buy milk - high").
# Lets them view the current list, delete tasks by number, and mark tasks as complete.
# Keeps looping until the user types “exit”.
# Shows a summary at the end: number of completed tasks vs pending.
# Skills practiced: lists, string parsing, loops, input, CRUD basics
todo_list = []

def show_tasks():
    if not todo_list:
        print("\n🗒️ No tasks in the list.")
    else:
        print("\n📋 Current To-Do List:")
        for idx, task in enumerate(todo_list, 1):
            status = "✅" if task["completed"] else "❌"
            print(f"{idx}. [{task['priority'].capitalize()}] {task['task']} - {status}")

def add_task():
    user_input = input("Enter task and priority (e.g., 'Buy milk - high'): ").strip()
    if '-' not in user_input:
        print("⚠️ Invalid format. Use 'task - priority'.")
        return
    task_text, priority = [part.strip() for part in user_input.split('-', 1)]
    priority = priority.lower()
    if priority not in ("low", "medium", "high"):
        print("⚠️ Priority must be 'low', 'medium', or 'high'.")
        return
    todo_list.append({"task": task_text, "priority": priority, "completed": False})
    print(f"✔️ Added: '{task_text}' with {priority} priority.")

def delete_task():
    show_tasks()
    if not todo_list:
        return
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(todo_list):
            removed = todo_list.pop(num - 1)
            print(f" Deleted: '{removed['task']}'")
        else:
            print(" Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_task_complete():
    show_tasks()
    if not todo_list:
        return
    try:
        num = int(input("Enter task number to mark complete: "))
        if 1 <= num <= len(todo_list):
            todo_list[num - 1]["completed"] = True
            print(f"✅ Marked '{todo_list[num - 1]['task']}' as complete.")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# Main loop
print("📝 Welcome to the To-Do List Manager!")
print("Available commands: add, view, delete, complete, exit")

while True:
    command = input("\nWhat would you like to do? ").strip().lower()

    if command == "add":
        add_task()
    elif command == "view":
        show_tasks()
    elif command == "delete":
        delete_task()
    elif command == "complete":
        mark_task_complete()
    elif command == "exit":
        break
    else:
        print("⚠️ Unknown command. Try: add, view, delete, complete, exit")

# Final Summary
completed = sum(1 for task in todo_list if task["completed"])
pending = len(todo_list) - completed

print("\n📊 Session Summary:")
print(f"✅ Completed tasks: {completed}")
print(f"❌ Pending tasks: {pending}")
print("👋 Goodbye!")
