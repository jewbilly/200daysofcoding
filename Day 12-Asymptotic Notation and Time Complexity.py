import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

n = np.linspace(1, 100, 200)
functions = {
    "O(1)": lambda n: np.ones_like(n),
    "O(log n)": lambda n: np.log2(n),
    "O(n)": lambda n: n,
    "O(n log n)": lambda n: n * np.log2(n),
    "O(n^2)": lambda n: n**2,
    "O(n^3)": lambda n: n**3
}

colors = ['green', 'blue', 'orange', 'purple', 'red', 'black']

fig, ax = plt.subplots()
lines = []

for color in colors:
    line, = ax.plot([], [], color=color, linewidth=2)
    lines.append(line)

def init():
    ax.set_xlim(1, 100)
    ax.set_ylim(0, 10000)
    ax.set_title('Growth of Different Time Complexities')
    ax.set_xlabel('n (input size)')
    ax.set_ylabel('Operations')
    return lines

def update(frame):
    for i, (label, func) in enumerate(functions.items()):
        lines[i].set_data(n[:frame], func(n[:frame]))
        lines[i].set_label(label)
    ax.legend()
    return lines

ani = FuncAnimation(fig, update, frames=len(n), init_func=init, blit=True, repeat=False)
plt.show()

#Code for each time complexity
# O(1) – Constant Time
def get_first_element(arr):
    return arr[0]

# O(log n) – Logarithmic Time (Binary Search)
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# O(n) – Linear Time
def find_element(arr, target):
    for i in arr:
        if i == target:
            return True
    return False

# O(n log n) – Linearithmic Time (Merge Sort)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = merge_sort(arr[:mid])
        R = merge_sort(arr[mid:])
        return merge(L, R)
    return arr

def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result + left + right

# O(n^2) – Quadratic Time (Bubble Sort)
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# O(n^k) – Polynomial Time (Nested Loops)
def polynomial_time(n, k):
    def helper(level, depth):
        if level == depth:
            return
        for i in range(n):
            helper(level + 1, depth)
    helper(0, k)
