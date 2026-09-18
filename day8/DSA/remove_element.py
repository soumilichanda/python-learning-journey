def remove_element(nums, val: int) -> int:
    writer = 0
    for reader in range(len(nums)):
        if nums[reader] != val:
            nums[writer] = nums[reader]
            writer += 1
    return writer


if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    val = 3
    k = remove_element(nums, val)
    print(f"k = {k}, nums = {nums[:k]}")