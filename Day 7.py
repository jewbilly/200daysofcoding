def nth_root(x, n, epsilon=0.00001):

    if x < 0 and n % 2 == 0:
        raise ValueError("Even root of negative number is not real.")
    
    sign = -1 if x < 0 else 1
    x = abs(x)

    low = 0
    high = max(1, x)
    guess = (low + high) / 2

    while abs(guess ** n - x) > epsilon:
        if guess ** n < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2

    return sign * guess

# Example usage

print("Cube root of 27:", round(nth_root(27, 3), 5))
print("4th root of 16:", round(nth_root(16, 4), 5))
print("5th root of -32:", round(nth_root(-32, 5), 5))
