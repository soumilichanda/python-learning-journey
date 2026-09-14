def count_even_odd(arr):
    even_count = 0
    odd_count = 0
    
    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
            
    return even_count, odd_count

# Test run
numbers = [12, 7, 5, 20, 9, 14, 3]
evens, odds = count_even_odd(numbers)

print(f"Even numbers count: {evens}")
print(f"Odd numbers count : {odds}")