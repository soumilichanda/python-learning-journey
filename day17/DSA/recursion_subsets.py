def subsets(nums: list[int]) -> list[list[int]]:
    result: list[list[int]] = []
    path: list[int] = []

    def backtrack(start_idx: int) -> None:
        # Every node in the decision tree represents a valid subset
        result.append(list(path))

        for i in range(start_idx, len(nums)):
            path.append(nums[i])       # Choose
            backtrack(i + 1)           # Explore (move forward to avoid duplicate subsets)
            path.pop()                 # Un-choose / Backtrack

    backtrack(0)
    return result


if __name__ == "__main__":
    test_nums = [1, 2, 3]
    all_subsets = subsets(test_nums)
    print(f"Subsets for {test_nums} (Total {len(all_subsets)}):")
    for s in all_subsets:
        print(s)