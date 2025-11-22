shopping_list = []
while True:
 print("\n=== Shopping List Manager ===")
 print("1. Add an item")
 print("2. Remove an item")
 print("3. View shopping list")
 print("4. Exit")
choice = input("Enter your choice (1-4):")
if choice == "1":
 item = input("Enter the item to add:")
 shopping_list.append(item)
 print(f"'{item}' has been added to your shopping list.")
elif choice == "2":
 item = input("Enter the item to remove:")
 if item in shopping_list:
  shopping_list.remove(item)
  print(f"'{item}' has been removed from your shopping list.")
 else:
  print(f"'{item}' was not found in the shopping list.")
elif choice == "3":
   print("\nYour Shopping List:")
   if not shopping_list:
    print("(The list is empty.)")
   else:
    for i, item in enumerate(shopping_list, 1):print(f"{i}.{item}")
elif choice == "4":
    print("Goodbye!")
    break
else:
 print("Invalid choice. Please enter a number between 1 and 4.")
