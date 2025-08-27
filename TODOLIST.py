import os

class TodoApp:
    def __init__(self):
        self.tasks = []

    def show_menu(self):
        print("\n===== TO-DO LIST APP =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Done")
        print("6. Exit")

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(self.tasks, 1):
                status = "✅ " if task["done"] else "❌"
                print(f"{i}. {task['title']} {status}")

    def add_task(self):
        title = input("\nEnter new task: ").strip()
        if title:
            self.tasks.append({"title": title, "done": False})
            print("Task added successfully!")
        else:
            print("Task cannot be empty!")

    def update_task(self):
        self.view_tasks()
        if self.tasks:
            try:
                index = int(input("\nEnter task number to update: ")) - 1
                if 0 <= index < len(self.tasks):
                    new_title = input("Enter updated task: ").strip()
                    if new_title:
                        self.tasks[index]["title"] = new_title
                        print("Task updated successfully!")
                    else:
                        print("Task cannot be empty!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    def delete_task(self):
        self.view_tasks()
        if self.tasks:
            try:
                index = int(input("\nEnter task number to delete: ")) - 1
                if 0 <= index < len(self.tasks):
                    removed = self.tasks.pop(index)
                    print(f"Task '{removed['title']}' deleted successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    def mark_done(self):
        self.view_tasks()
        if self.tasks:
            try:
                index = int(input("\nEnter task number to mark as done: ")) - 1
                if 0 <= index < len(self.tasks):
                    self.tasks[index]["done"] = True
                    print(f"Task '{self.tasks[index]['title']}' marked as done ✔")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    def run(self):
        while True:
            self.show_menu()
            choice = input("\nChoose an option: ")
            if choice == "1":
                self.view_tasks()
            elif choice == "2":
                self.add_task()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.mark_done()
            elif choice == "6":
                print("Exiting To-Do List App. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = TodoApp()
    app.run()
