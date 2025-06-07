# URL: Click here
# ID: 915a6bae2bcd995ff98d6de09b435502fa78c475
# Author: Adeola Olanrewaju
# Subject: Add shopping list manager script
# Date: 2025-06-07 21:05:24 +0100

# ------------------------
# CHECKS:
# - Checks for file exists and not empty ✅
# - Checks for definition of the display_menu ✅
# - Checks for implementation of an array shopping_list ✅
# - Checks for calling display_menu function ✅
# - Checks for implementation of Choice Input as a number ✅
# ------------------------

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice (number 1–4): ").strip()

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added.")
            else:
                print("Item name cannot be empty.")

        elif choice == '2':
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed.")
            else:
                print(f"'{item}' is not in your shopping list.")

        elif choice == '3':
            if shopping_list:
                print("\nYour Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is currently empty.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
