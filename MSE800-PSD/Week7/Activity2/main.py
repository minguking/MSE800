from aquarium import Aquarium

## Main
def main():
    aquarium = Aquarium()
    
    print("=== Auckland Aquarium Management System ===\n")
    
    while True:
        print("Options:")
        print("1. Add fish")
        print("2. View inventory by category")
        print("3. View all fish")
        print("4. Clear aquarium")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            fish_type = input("Enter fish type (goldfish, shark, angelfish, tuna, salmon): ").strip()
            try:
                count = int(input("Enter number of fish to add: ").strip())
                if count <= 0:
                    print("Please enter a positive number!\n")
                    continue
                aquarium.add_fish(fish_type, count)
                print(f"Added {count} {fish_type}(s) to the aquarium!\n")
            except ValueError as e:
                print(f"Error: {e}\n")
        
        elif choice == "2":
            aquarium.display_inventory()
        
        elif choice == "3":
            aquarium.display_all_fish()
        
        elif choice == "4":
            confirm = input("Are you sure you want to clear the aquarium? (yes/no): ").strip().lower()
            if confirm == "yes":
                aquarium.clear()
                print("Aquarium cleared!\n")
            else:
                print("Cancelled.\n")
        
        elif choice == "5":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.\n")


if __name__ == "__main__":
    main()
