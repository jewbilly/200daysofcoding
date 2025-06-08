#Original Funtion
def find_root(number):
    for i in range(abs(number) + 1):
        if i ** 3 == abs(number):
            return i if number >= 0 else -i
    return None
#Modular Funtion
def is_perfect_cube(n):
    """Check if n is a perfect cube."""
    abs_n = abs(n)
    for i in range(abs_n + 1):
        if i ** 3 == abs_n:
            return True
        elif i ** 3 > abs_n:
            break
    return False

def cube_root(n):
    """Return the cube root if n is a perfect cube, otherwise None."""
    abs_n = abs(n)
    for i in range(abs_n + 1):
        if i ** 3 == abs_n:
            return i if n >= 0 else -i
    return None

def find_root(n):
    """Wrapper function that returns cube root or error message."""
    if is_perfect_cube(n):
        return cube_root(n)
    else:
        return f"{n} is not a perfect cube"
#Example Usage
numbers = [27, -8, 10, 64]

for num in numbers:
    print(f"Cube root of {num}: {find_root(num)}")
