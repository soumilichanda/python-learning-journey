def find_peak_element(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left


if __name__ == "__main__":
    nums = [1, 2, 1, 3, 5, 6, 4]
    peak_idx = find_peak_element(nums)
    print(f"Peak index: {peak_idx} (Value: {nums[peak_idx]})")