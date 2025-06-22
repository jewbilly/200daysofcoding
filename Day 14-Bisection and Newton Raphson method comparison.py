import math

# Function definition
def f(x):
    return 4 * x + math.sin(x) - math.exp(x)

# Derivative for Newton-Raphson
def df(x):
    return 4 + math.cos(x) - math.exp(x)

# Newton-Raphson method
def newton_raphson(x0, tol=1e-6, max_iter=500):
    steps = 0
    xk = x0
    while steps < max_iter:
        fx = f(xk)
        dfx = df(xk)
        if dfx == 0:
            return None, steps
        xk_next = xk - fx / dfx
        err = abs(xk_next - xk) / abs(xk_next)
        xk = xk_next
        steps += 1
        if err < tol:
            return xk, steps
    return None, steps

# Bisection method
def bisection(a, b, tol=1e-6, max_iter=500):
    steps = 0
    if f(a) * f(b) > 0:
        return None, steps  # Invalid interval

    while steps < max_iter:
        c = (a + b) / 2
        fc = f(c)
        err = abs(b - a) / 2

        if fc == 0 or err < tol:
            return c, steps + 1

        if f(a) * fc < 0:
            b = c
        else:
            a = c
        steps += 1

    return None, steps

# Comparison function
def compare_methods(x0, a, b):
    print("Comparing Newton-Raphson vs Bisection Method\n")

    root_nr, steps_nr = newton_raphson(x0)
    root_bi, steps_bi = bisection(a, b)

    print(f"Newton-Raphson: root = {root_nr}, steps = {steps_nr}")
    print(f"Bisection      : root = {root_bi}, steps = {steps_bi}")

# Example usage
if __name__ == "__main__":
    x0 = float(input("Enter initial guess for Newton-Raphson: "))
    a = float(input("Enter lower bound for Bisection: "))
    b = float(input("Enter upper bound for Bisection: "))
    compare_methods(x0, a, b)
