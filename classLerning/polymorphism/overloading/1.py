# Example 1: Function Overloading with default arguments


def add(a, b=0, c=0):
    return a + b + c

print(add(2))       # 2
print(add(2, 3))    # 5
print(add(2, 3, 4)) # 9
