# Approach 1: Using Slicing (Clean & Pythonic)
def reverse_list_slicing(arr):
    return arr[::-1]

# Approach 2: Using a Loop (Algorithmic / Interview Style)
def reverse_list_loop(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

# Test run
numbers = [10, 20, 30, 40, 50]
print("Reversed (Slicing):", reverse_list_slicing(numbers))
print("Reversed (Loop):   ", reverse_list_loop(numbers))