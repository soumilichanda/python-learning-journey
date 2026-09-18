def find_floor_ceiling(arr, x):
    left, right = 0, len(arr) - 1
    floor_val, ceil_val = None, None

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return arr[mid], arr[mid]
        elif arr[mid] < x:
            floor_val = arr[mid]
            left = mid + 1
        else:
            ceil_val = arr[mid]
            right = mid - 1

    return floor_val, ceil_val


if __name__ == "__main__":
    arr = [1, 4, 6, 8, 10, 15, 19]
    x = 5
    floor_val, ceil_val = find_floor_ceiling(arr, x)
    print(f"Floor: {floor_val}, Ceiling: {ceil_val}")