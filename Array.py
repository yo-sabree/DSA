"""
Demonstration of all major operations on Python's built-in `array` module.
Array type used: array('i') → signed integer array
Time and space complexities follow standard dynamic-array behavior.
"""

import array

# ---------------------------------------------------------------------------
# Array Creation
# ---------------------------------------------------------------------------

# Create an array of integers
arr = array.array('i', [10, 20, 30, 40, 50])  # O(n) time, O(n) space
print("Original array:", arr)


# ---------------------------------------------------------------------------
# Accessing Elements (Indexing)
# ---------------------------------------------------------------------------

# Access element at index (Random access)
print("Element at index 2:", arr[2])  # O(1) time, O(1) space


# ---------------------------------------------------------------------------
# Modifying Elements
# ---------------------------------------------------------------------------

arr[1] = 25   # Update element → O(1) time, O(1) space
print("After modification:", arr)


# ---------------------------------------------------------------------------
# Inserting Elements
# ---------------------------------------------------------------------------

# Insert at specific index 
arr.insert(2, 99)  
# Worst-case O(n) time due to shifting, O(1) space (amortized)
print("After insert at index 2:", arr)

# Append at end
arr.append(60)  
# Amortized O(1) time, O(1) space
print("After append:", arr)

# Extend using another list
arr.extend([70, 80])  
# O(k) time for k new elements, O(k) space
print("After extend:", arr)


# ---------------------------------------------------------------------------
# Removing Elements
# ---------------------------------------------------------------------------

# Remove first occurrence of a value
arr.remove(99)  
# O(n) time (search) + O(n) time (shift) → O(n) total, O(1) space
print("After remove 99:", arr)

# Pop last element
popped = arr.pop()  
# O(1) time, O(1) space
print("Popped:", popped, "| After pop:", arr)

# Pop at specific index
popped_index = arr.pop(1)  
# O(n) time due to shifting, O(1) space
print("Popped index 1:", popped_index, "| After pop:", arr)


# ---------------------------------------------------------------------------
# Searching
# ---------------------------------------------------------------------------

# Linear search for value
idx = arr.index(40)  
# O(n) time, O(1) space
print("Index of 40:", idx)


# ---------------------------------------------------------------------------
# Slicing (Creates a new array)
# ---------------------------------------------------------------------------

sliced_arr = arr[1:4]  
# O(k) time and O(k) space for slice of size k
print("Sliced array [1:4]:", sliced_arr)


# ---------------------------------------------------------------------------
# Reverse
# ---------------------------------------------------------------------------

arr.reverse()  
# O(n) time, O(1) space
print("Reversed array:", arr)


# ---------------------------------------------------------------------------
# Buffer Info (Low-level details)
# ---------------------------------------------------------------------------

# Returns (memory_address, length)
print("Buffer info:", arr.buffer_info())  # O(1)


# ---------------------------------------------------------------------------
# Convert to Python List
# ---------------------------------------------------------------------------

lst = arr.tolist()  
# O(n) time, O(n) space
print("Converted to list:", lst)


# ---------------------------------------------------------------------------
# Count occurrences
# ---------------------------------------------------------------------------

count_40 = arr.count(40)  
# O(n) time, O(1) space
print("Count of 40:", count_40)


# ---------------------------------------------------------------------------
# Concatenation (using +)
# ---------------------------------------------------------------------------

new_arr = arr + array.array('i', [100, 200])  
# O(n + m) time, O(n + m) space
print("Concatenated array:", new_arr)


# ---------------------------------------------------------------------------
# Iteration
# ---------------------------------------------------------------------------

# O(n) time, O(1) space
for val in arr:
    print("Iterated value:", val)


# ---------------------------------------------------------------------------
# Length of array
# ---------------------------------------------------------------------------

print("Length of array:", len(arr))  # O(1)
