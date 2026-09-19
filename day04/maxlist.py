def find_maximum(arr):
    if not arr:
        return None
    
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
            
    return max_val

# Test run
numbers = [5, 8, 2, 90, 1]
print("Maximum Element:", find_maximum(numbers))