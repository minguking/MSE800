"""
MSE800-PSD | Week 1 - Activity 3
Power Calculator: calculate x to the power of y
"""

def power(x, y):
    """
    Calculate x raised to the power of y.

    Args:
        x (float): The base number
        y (float): The exponent

    Returns:
        float: Result of x ** y
    """
    return x ** y


def main():
    print("=" * 40)
    print("   MSE800-PSD | Power Calculator")
    print("=" * 40)

    try:
        x = float(input("Enter base (x): "))
        y = float(input("Enter exponent (y): "))

        result = power(x, y)

        print(f"\n  {x} ^ {y} = {result}")
        print("=" * 40)

    except ValueError:
        print("Error: Please enter valid numbers.")


if __name__ == "__main__":
    main()