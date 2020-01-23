def take_input_for_new_task():
  date = input("Input Reminder Date(ddmmyyyy)Ex:31122020:: ")
  description = input("Description:: ")
  print("input date: ", date)
  print("input description: ", description)
  return [date, description]

def handleCreateNewReminder(self):
  task = self.take_input_for_new_task()
  print(task)

  print("TODO: save the event in db")
  input()

def print_task_detail(task):
  try:
    print("Task ID#: ", task[0])
    print("Date: ", task[1])
    print("Description: ", task[2])
  except Exception:
    print("")
  input("\nPress any key to continue ...\n")

def search_task_by_task_id(task_id):
  print("TODO: search a task and print its details")
  task = ["828902", "31122020", "sample task description!!!!!!!!"]
  print_task_detail(task)

def handle_update_reminder():
  description = input("Input Description to search(wildcard search):: ")
  print("TODO: Search in db and print the ooutput")
  task_id = input("Input task no# to edit:: ")
  search_task_by_task_id(task_id)
  print("\n\nUpdate new task details\n\n")
  updated_task = take_input_for_new_task()
  print("TODO: save the event in db")
  print_task_detail(updated_task)
  print("TODO: update event to DB ")
  input("\nPress any key to continue ...\n")

def handle_up_coming_events():
  print("handle upcoming event")
  print("TODO: get current date in format 'DDMMYYYY'")
  print("handle upcoming event")
  input("\nPress any key to continue ...\n")

def handle_delete_events():
  description = input("Input Description to search(wildcard search):: ")
  print("TODO: Search in db and print the output")
  task_id = input("Input task no# to delete:: ")
  search_task_by_task_id(task_id)
  choice = input("Are you sure to delete (y/n)::")
  if choice == "y":
    print("\n\ndeleting record ...\n\n")

  input("\nPress any key to continue ...\n")

def handle_history_record():
  print("TODO: Search history from Database")
  input("\nPress any key to continue ...\n")

def print_menu():
  while True:
    print("Welcome to todo list")
    print("1.Create new reminder")
    print("2.update event")
    print("3.up coming events")
    print("4.delete event")
    print("5.history events")
    print("6.bye bye...")
    choice = input()

    if choice == '1':
      handleCreateNewReminder()

    elif choice == '2':
      handle_update_reminder()

    elif choice == '3':
      handle_up_coming_events()

    elif choice == '4':
      handle_delete_events()

    elif choice == '5':
      handle_history_record()

    elif choice == str(6):
      break

print_menu()

