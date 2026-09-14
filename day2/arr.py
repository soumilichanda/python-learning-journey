arr = [12, 8, 25, 5, 90]

# Initialize variables using the first element
largest = arr[0]
smallest = arr[0]
total_sum = 0

for num in arr:
    # Update largest
    if num > largest:
        largest = num
        
    # Update smallest
    if num < smallest:
        smallest = num
        
    # Accumulate sum for average calculation
    total_sum += num

# Calculate average
average = total_sum / len(arr)

# Output Results
print(f"Largest  = {largest}")
print(f"Smallest = {smallest}")
print(f"Average  = {average}")