from abc import ABC, abstractmethod

## Parent Class ##
class Fish(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

    @property
    @abstractmethod
    def category(self) -> str:
        pass
    
    def __str__(self):
        return f"{self.name} is a {self.category} fish."


class GoldFish(Fish):
    def __init__(self, name):
        super().__init__("Gold Fish")

    @property
    def category(self) -> str:
        return "Beautiful"
    
class Shark(Fish):
    def __init__(self, name):
        super().__init__("Shark")

    @property
    def category(self) -> str:
        return "Dangerous"

class Angelfish(Fish):
    def __init__(self, name):
        super().__init__("Angelfish")

    @property
    def category(self) -> str:
        return "Beautiful"

class Tuna(Fish):
    def __init__(self, name):
        super().__init__("Tuna")

    @property
    def category(self) -> str:
        return "Edible"

class Salmon(Fish):
    def __init__(self, name):
        super().__init__("Salmon")

    @property
    def category(self) -> str:
        return "Edible"


## Factory Pattern ##
class FishFactory:
    _fish_map = {
        "goldfish":  GoldFish,
        "shark":     Shark,
        "angelfish": Angelfish,
        "tuna":      Tuna,
        "salmon":    Salmon,
    }

    @staticmethod
    def create(fish_type: str) -> Fish:
        key = fish_type.strip().lower()
        cls = FishFactory._fish_map.get(key)
        if cls is None:
            available = ", ".join(FishFactory._fish_map.keys())
            raise ValueError(f"Unknown fish type: {fish_type}. Available: {available}")
        return cls(fish_type)


## Singleton Pattern ##

class Aquarium:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._fish_list = []
        return cls._instance
    
    def add_fish(self, fish_type: str, count: int = 1):
        """Add fish to the aquarium"""
        for _ in range(count):
            fish = FishFactory.create(fish_type)
            self._fish_list.append(fish)
    
    def display_inventory(self):
        """Display fish categories and their counts"""
        if not self._fish_list:
            print("The aquarium is empty!")
            return
        
        category_count = {}
        for fish in self._fish_list:
            category = fish.category
            category_count[category] = category_count.get(category, 0) + 1
        
        print("\n=== Aquarium Inventory ===")
        for category, count in sorted(category_count.items()):
            print(f"{category}: {count} fish")
        print(f"Total: {len(self._fish_list)} fish\n")
    
    def display_all_fish(self):
        """Display fish summary by type in the aquarium"""
        if not self._fish_list:
            print("The aquarium is empty!")
            return
        
        fish_summary = {}
        for fish in self._fish_list:
            key = (fish.name, fish.category)
            fish_summary[key] = fish_summary.get(key, 0) + 1

        print("\n=== Fish Summary in Aquarium ===")
        for (name, category), count in sorted(fish_summary.items()):
            fish_label = f"{name}s" if count != 1 else name
            article = "an" if category[0].lower() in "aeiou" else "a"
            print(f"We have {count} {fish_label}, {name} is {article} {category.lower()} fish.")
        print()
    
    def clear(self):
        """Clear all fish from the aquarium"""
        self._fish_list.clear()
    
    def get_total_count(self) -> int:
        """Get total number of fish"""
        return len(self._fish_list)


## Main ##

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
