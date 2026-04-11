# MSE800-PSD | Week 1 – Activity 3: Power Calculator

## Description

This project is a simple Python command-line application that calculates the power of a number.  
Given a **base** `x` and an **exponent** `y`, the program computes and displays `x ^ y`.

It was developed as part of the **MSE800 Professional Software Development** course.

---

## Project Structure

```
MSE800-PSD/
└── Week1/
    ├── power_calculator.py   # Main Python script
    └── README.md             # This file
```

---

## How to Run

Make sure Python 3 is installed, then run:

```bash
python power_calculator.py
```

You will be prompted to enter the base and exponent values:

```
========================================
   MSE800-PSD | Power Calculator
========================================
Enter base (x): 3
Enter exponent (y): 4

  3.0 ^ 4.0 = 81.0
========================================
```

---

## Code Overview

```python
def power(x, y):
    return x ** y
```

The core logic uses Python's built-in `**` operator to compute the power.  
The `main()` function handles user input and displays the result with error handling for invalid entries.

---

## Environment

| Item        | Details                        |
|-------------|--------------------------------|
| Language    | Python                         |
| IDE         | VS Code                        |
| Python Ver. | Python3.13.3                   |

---