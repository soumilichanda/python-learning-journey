def next_greater_element(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [-1] * n
    stack = []  # Stores indices in monotonic decreasing order

    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)

    return result


if __name__ == "__main__":
    nums1 = [4, 5, 2, 25]
    nums2 = [13, 7, 6, 12]
    print(f"{nums1} -> {next_greater_element(nums1)}")
    print(f"{nums2} -> {next_greater_element(nums2)}")