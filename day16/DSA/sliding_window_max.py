from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0:
        return []

    dq = deque()  # Stores indices in monotonic decreasing order of values
    result = []

    for i in range(len(nums)):
        # Evict indices outside current window
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Evict smaller values from tail to preserve descending invariant
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        # Append window max once full window length is reached
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


if __name__ == "__main__":
    test_nums = [1, 3, -1, -3, 5, 3, 6, 7]
    window = 3
    print("Sliding Window Maxima:", max_sliding_window(test_nums, window))