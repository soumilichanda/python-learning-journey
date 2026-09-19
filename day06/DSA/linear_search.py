def linear_search(arr, target):
    for item in arr:
        if item == target:
            return True
    return False

# Test run
arr = [10, 20, 30, 40, 50]
target = 30
print("Found" if linear_search(arr, target) else "Not Found")