# Factory Pattern Example

This example shows a simple implementation of the Factory Pattern in Python.

## What it does

- Defines an abstract `Factory` class for creating products.
- Implements `DogFactory` and `CatFactory` to create `Dog` and `Cat` objects.
- Implements `AnimalFactory` to create either a `Dog` or `Cat` based on a string input.
- Defines `Dog` and `Cat` classes that both implement a `run()` method.

## How to run

```bash
python factory_pattern.py
```

## Expected output

```
I'm a Dog, I can run!!
I'm a Cat, I can run!!
I'm a Dog, I can run!!
```

## Notes

- `DogFactory` always returns a `Dog`.
- `CatFactory` always returns a `Cat`.
- `AnimalFactory` returns a `Dog` or `Cat` depending on the `kind` argument.
- This example demonstrates how a factory can hide object creation logic and let the client code just call `create_product()`.
