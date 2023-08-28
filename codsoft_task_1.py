# Create an empty list to store tasks
tasks = []

while True: 
     print("\nOptions:")
     print("1. Add Task")
     print("2. Remove Task")
     print("3. Show Task")
     print("4. Quit")

     choice = input("\nEnter your choice: ")

     if choice == "1":
          task_name = input("Enter the task: ")
          tasks.append(task_name)
          print("Task added!")
          
     elif choice == "2":
          if len(tasks) > 0:
               task_index = int(input("Enter the task number to remove: ")) - 1
               if 0 <= task_index < len(tasks):
                    removed_task = tasks.pop(task_index)
                    print(f"Task '{removed_task}' removed!")
               else:
                    print("Invalid task number.")
          else:
               print("No tasks to remove.")
               
     elif choice == "3":
          print("To-Do List:")
          for index, task in enumerate(tasks, start=1):
               print(f"{index}. {task}")
          
     elif choice == "4":
          print("Goodbye!...Have a nice day")
          break
     else:
          print("Invalid choice. Please choose a valid option.")
