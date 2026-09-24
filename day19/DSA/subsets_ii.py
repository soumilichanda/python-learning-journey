def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result: list[list[int]] = []
    path: list[int] = []

    def backtrack(start_idx: int) -> None:
        result.append(list(path))

        for i in range(start_idx, len(nums)):
            # Skip identical values to prevent duplicate subsets
            if i > start_idx and nums[i] == nums[i - 1]:
                continue

            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

    backtrack(0)
    return result


if __name__ == "__main__":
    test_nums = [1, 2, 2]
    unique_subsets = subsets_with_dup(test_nums)
    print(f"Subsets with duplicates handled for {test_nums} (Total {len(unique_subsets)}):")
    for s in unique_subsets:
        print(s)