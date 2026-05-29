# Week 7 Activity 2 - Aquarium Management

This project manages an aquarium in Auckland with different fish types: Goldfish, Shark, Angelfish, Tuna, and Salmon.

## Project structure

- `main.py` - program entry point and user menu.
- `aquarium.py` - `Aquarium` singleton class for managing the aquarium inventory.
- `fish.py` - fish classes and the `FishFactory` factory implementation.
- `README.md` - project description and usage instructions.

## Classes and responsibilities

- `Fish` (abstract base class)
  - Common parent for all fish types.
  - Requires each fish type to implement a `category` property.

- `GoldFish`, `Shark`, `Angelfish`, `Tuna`, `Salmon`
  - Specific fish subclasses in `fish.py`.
  - Each class defines its own `category`:
    - `GoldFish` and `Angelfish` are `Beautiful` fish.
    - `Shark` is `Dangerous`.
    - `Tuna` and `Salmon` are `Edible`.

- `FishFactory`
  - Factory pattern implementation in `fish.py`.
  - Creates the correct fish object based on a string type.

- `Aquarium`
  - Singleton pattern implementation in `aquarium.py`.
  - Keeps a single aquarium instance for all fish data.
  - Adds fish and shows inventory summaries.

## Description

- Uses Factory and Singleton design patterns.
- Adds fish to the aquarium and keeps a single shared inventory.
- Displays category counts and fish summaries by type.
- Avoids repeated listing by summarizing fish like "We have 60 Salmons, Salmon is an edible fish."

## How to run

```bash
python main.py
```

## Notes

- `main.py` is the program entry point, while `aquarium.py` and `fish.py` contain the core logic.
