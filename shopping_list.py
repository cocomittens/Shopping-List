shopping_list = []

# Move an item in the list
def move_item(idx_from, idx_to):
  index_from = idx_from - 1
  index_to = idx_to - 1
  item = shopping_list.pop(index_from)
  shopping_list.insert(index_to, item)
  print("{} moved from position {} to position {}".format(item, idx_from, idx_to))

# Remove an item from the list
def remove_item(idx):
  index = idx - 1
  item = shopping_list.pop(index)
  print("Remove {}.".format(item))

# Show possible commands
def show_help():
  print("\nSeparate each item with a comma.")
  print("Type DONE to quit, SHOW to see the current list, SHIFT to move an item to another position on the list, REMOVE to remove an item from the list, CLEAR to remove everything from the list, and HELP to get this message.")

# Print the current list
def show_list():
  count = 1
  for item in shopping_list:
    print("{}. {}".format(count, item))
    count += 1

print("Hi! Welcome to the shopping list. Give me a list of things you want to shop for.")
show_help()

while True:
  # Get new item to add to list
  new_stuff = input("> ")

  # DONE: Print list and quit program
  if new_stuff == "DONE":
    print("\nHere's your list:")
    show_list()
    break
  # HELP: Show possible commands
  elif new_stuff == "HELP":
    show_help()
    continue
  # SHOW: Print list and continue
  elif new_stuff == "SHOW":
    show_list()
    continue
  # SHIFT: Move an item to another position on the list
  elif new_stuff == "SHIFT":
    idx_from = input("Enter the number of the item you wish to move: ")
    idx_to = input("Enter the position you wish to move it to: ")
    move_item(int(idx_from), int(idx_to))
    continue
  # REMOVE: Remove an item from the list
  elif new_stuff == "REMOVE":
    show_list()
    idx = input("Enter the number of the item you wish to remove: ")
    remove_item((int(idx)))
    continue
  # CLEAR: Remove all items from the list
  elif new_stuff == "CLEAR":
    shopping_list.clear()
    print("List cleared.")
    continue
  # Add entered items) to list
  else:
    # Entered items to be added to list
    new_list = new_stuff.split(",")
    # Index at which entered items are to be added
    index = input("Add this at a certain spot? Press enter for the end of the list, or give me a number. Currently {} items in the list.  ".format(len(shopping_list)))
    # Add item(s) to specific index of the list
    if index:
      spot = int(index) - 1
      for item in new_list:
        shopping_list.insert(spot, item.strip())
        spot += 1
    # Add item(s) to the end of the list
    else:
      for item in new_list:
        shopping_list.append(item.strip())
