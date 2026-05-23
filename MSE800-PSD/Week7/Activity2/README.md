# Week 7 Activity 2 - Aquarium Management

This project manages an aquarium in Auckland with different fish types: Goldfish, Shark, Angelfish, Tuna, and Salmon.

## Project structure

- `aquarium.py` - main application file with the aquarium menu, factory, and singleton implementation.
- `fish.py` - fish classes and the base `Fish` abstract class.
- `README.md` - project description and usage instructions.

## Classes and responsibilities

- `Fish` (abstract base class)
  - Common parent for all fish types.
  - Requires each fish to implement a `category` property.

- `GoldFish`, `Shark`, `Angelfish`, `Tuna`, `Salmon`
  - Specific fish subclasses in `fish.py`.
  - Each class sets its own `category` value:
    - `GoldFish` and `Angelfish` are `Beautiful` fish.
    - `Shark` is `Dangerous`.
    - `Tuna` and `Salmon` are `Edible`.

- `FishFactory`
  - Factory pattern implementation in `aquarium.py`.
  - Creates fish objects from a string type.

- `Aquarium`
  - Singleton pattern implementation in `aquarium.py`.
  - Stores all fish in a single aquarium inventory.
  - Provides methods to add fish, display inventory, and summarize fish.

## Description

- Uses design patterns to create and manage fish objects.
- Displays fish categories and counts in the aquarium.
- Supports adding multiple fish in one request.
- Shows a summary like "We have 60 Salmons, Salmon is an edible fish."

## How to run

```bash
python aquarium.py
```

## Notes

- A README file is mandatory and must be included in your GitHub repository for this activity.
- The project combines both Factory and Singleton patterns to manage fish creation and aquarium state.
