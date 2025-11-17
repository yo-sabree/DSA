def countdown(n):
    if n == 0:
        print("Done")
        return
    print(n)
    countdown(n - 1)

countdown(5)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

def recursive_sum(arr, depth=0):
    print("   " * depth, "recursive_sum(", arr, ")")
    if len(arr) == 0:
        print("   " * depth, "→ return 0")
        return 0
    result = arr[0] + recursive_sum(arr[1:], depth+1)
    print("   " * depth, f"→ return {arr[0]} + {result - arr[0]} = {result}")
    return result

print("Sum of array elements:", recursive_sum([1, 2, 3, 4, 5]))