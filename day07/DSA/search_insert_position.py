def search_insert(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


if __name__ == "__main__":
    arr = [1, 3, 5, 6]
    print(search_insert(arr, 5))
    print(search_insert(arr, 2))
    print(search_insert(arr, 7))