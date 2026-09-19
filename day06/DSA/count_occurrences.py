def count_occurrences(arr, target):
    """
    Counts the occurrences of target in arr.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count

# Test runs
arr = [4, 7, 4, 2, 7, 4, 9]
target = 4
result = count_occurrences(arr, target)
print(f"{target} occurs {result} times")