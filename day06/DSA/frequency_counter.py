def get_frequencies(arr):
    """
    Computes element frequencies using a dictionary hash map.
    Time Complexity: O(n) - each lookup and update is O(1) average.
    Space Complexity: O(k) - where k is the number of distinct elements.
    """
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq

# Test run
if __name__ == "__main__":
    arr = [10, 20, 10, 30, 20, 10, 40]
    frequencies = get_frequencies(arr)
    
    for key, count in frequencies.items():
        print(f"{key} -> {count}")