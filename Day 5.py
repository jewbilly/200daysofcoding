
import time
import math
import matplotlib.pyplot as plt

# --------------------------
# Cube root function
# --------------------------
def cube_root(n):
    """Find cube root of integer n using binary search.
    Works for negative numbers too. Returns steps taken."""
    
    steps = 0
    sign = -1 if n < 0 else 1
    n = abs(n)

    low = 0
    high = max(1, n)
    epsilon = 0.0001

    while low <= high:
        steps += 1
        mid = (low + high) / 2
        mid_cubed = mid ** 3

        if abs(mid_cubed - n) < epsilon:
            return sign * mid, steps
        elif mid_cubed < n:
            low = mid
        else:
            high = mid

        if abs(high - low) < epsilon:
            break

    return sign * mid, steps

# --------------------------
# Primality check
# --------------------------
def is_prime(n):
    """Efficient primality test using 6k +/- 1 rule."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_primes(limit):
    return sum(x for x in range(3, limit) if is_prime(x))

# --------------------------
# Graphing cube root performance
# --------------------------
def test_cube_root_performance():
    digit_counts = list(range(1, 10))
    steps_list = []
    time_list = []

    for d in digit_counts:
        number = 10**d - 1
        start_time = time.time()
        _, steps = cube_root(number)
        elapsed = time.time() - start_time

        steps_list.append(steps)
        time_list.append(elapsed)

    # Plot steps
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(digit_counts, steps_list, marker='o')
    plt.title('Steps vs Number of Digits')
    plt.xlabel('Number of Digits')
    plt.ylabel('Steps Taken')

    # Plot time
    plt.subplot(1, 2, 2)
    plt.plot(digit_counts, time_list, marker='o', color='green')
    plt.title('Execution Time vs Number of Digits (Python)')
    plt.xlabel('Number of Digits')
    plt.ylabel('Time (s)')

    plt.tight_layout()
    plt.show()

# --------------------------
# Run everything
# --------------------------
if __name__ == "__main__":
    print("Cube root of -27:")
    root, steps = cube_root(-27)
    print(f"Cube root: {root:.4f}, Steps taken: {steps}\n")

    print("Sum of primes between 3 and 1000:")
    print(sum_primes(1000))

    print("\nTesting performance...")
    test_cube_root_performance()