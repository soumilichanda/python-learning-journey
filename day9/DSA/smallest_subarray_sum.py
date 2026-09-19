def smallest_subarray_with_given_sum(s: int, arr: list[int]) -> int:
    min_length = float("inf")
    window_sum = 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1

    return min_length if min_length != float("inf") else 0


if __name__ == "__main__":
    arr = [2, 1, 5, 2, 3, 2]
    s = 7
    print(smallest_subarray_with_given_sum(s, arr))  # 2