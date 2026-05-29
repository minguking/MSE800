from fish import Fish, GoldFish, Shark, Angelfish, Tuna, Salmon, FishFactory

## Singleton Pattern
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
