
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed."

def modulo(x, y):
    if y != 0:
        return x % y
    else:
        return "Error: Division by zero is not allowed."

print('add', add(10, 5))
print('subtract', subtract(10, 5))
print('multiply', multiply(2, 7))
print('divide', divide(10, 4))
print('modulo', modulo(11, 3))