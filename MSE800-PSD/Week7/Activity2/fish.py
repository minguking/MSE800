from abc import ABC, abstractmethod

# Parent Class ##
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

