class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task, priority):
        if priority not in self.tasks:
            self.tasks[priority] = []
        self.tasks[priority].append(task)

    def remove_task(self, task):
        for priority in self.tasks:
            if task in self.tasks[priority]:
                self.tasks[priority].remove(task)
                if not self.tasks[priority]:
                    del self.tasks[priority]
                return True
        return False

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the To-Do List.")
        else:
            for priority in sorted(self.tasks.keys(), reverse=True):
                print(f"Priority {priority}:")
                for task in self.tasks[priority]:
                    print(f"- {task}")

def main():
    to_do_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Show Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            priority = int(input("Enter the priority (1-5, where 1 is highest): "))
            to_do_list.add_task(task, priority)
            print("Task added successfully.")

        elif choice == '2':
            task = input("Enter the task to remove: ")
            if to_do_list.remove_task(task):
                print("Task removed successfully.")
            else:
                print("Task not found.")

        elif choice == '3':
            to_do_list.show_tasks()

        elif choice == '4':
            print("Exiting the To-Do List application.")
            break

        else:
            print("Invalid choice. Please choose a valid option (1-4).")

if __name__ == "__main__":
    main()
