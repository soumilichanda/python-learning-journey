def find_second_largest(arr):
    """
    Finds second largest element in a single pass without sorting or max().
    Time Complexity: O(n) - visits each element once.
    Space Complexity: O(1) - tracks two numeric values.
    """
    if len(arr) < 2:
        return None

    first = float('-inf')
    second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    return second if second != float('-inf') else None

# Test run
if __name__ == "__main__":
    arr = [5, 8, 2, 10, 3]
    print(f"Second Largest = {find_second_largest(arr)}")