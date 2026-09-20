def merge(left: list[int], right: list[int]) -> list[int]:
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    sorted_arr = merge_sort(arr)
    print("Sorted Array:", sorted_arr)