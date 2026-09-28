from bisect import bisect_left


def length_of_lis(nums: list[int]) -> int:
    if not nums:
        return 0

    tails: list[int] = []

    for x in nums:
        idx = bisect_left(tails, x)
        if idx == len(tails):
            tails.append(x)
        else:
            tails[idx] = x

    return len(tails)


if __name__ == "__main__":
    test_arr = [10, 9, 2, 5, 3, 7, 101, 18]
    result = length_of_lis(test_arr)
    print("=== Longest Increasing Subsequence (O(n log n)) ===")
    print(f"Array: {test_arr}")
    print(f"LIS Length: {result} (Expected: 4 -> [2, 3, 7, 101] or [2, 5, 7, 101])")