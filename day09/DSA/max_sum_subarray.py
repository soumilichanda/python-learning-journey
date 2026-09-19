def max_sub_array_of_size_k(k: int, arr: list[int]) -> int:
    if not arr or k <= 0 or k > len(arr):
        return 0

    max_sum = 0
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        if window_sum > max_sum:
            max_sum = window_sum

    return max_sum


if __name__ == "__main__":
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    print(max_sub_array_of_size_k(k, arr))  # 9