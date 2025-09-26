def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item_to_add = input("Enter the item to add: ")
            shopping_list.append(item_to_add)
            print(f"'{item_to_add}' has been added to the list.")
        elif choice == '2':
            item_removed = input("Enter the name of the item you want to remove: ")
            if item_removed in shopping_list:
                shopping_list.remove(item_removed)
                print(f"'{item_removed}' has been removed from your shopping list.")
            else:
                print(f"'{item_removed}' is not in your shopping list.")
        elif choice == '3':
            if shopping_list:
                print("Your Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("Your shopping list is empty.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()