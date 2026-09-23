def permute(nums: list[int]) -> list[list[int]]:
    result: list[list[int]] = []
    path: list[int] = []
    used: list[bool] = [False] * len(nums)

    def backtrack() -> None:
        if len(path) == len(nums):
            result.append(list(path))
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            used[i] = True
            path.append(nums[i])
            backtrack()
            path.pop()
            used[i] = False

    backtrack()
    return result


if __name__ == "__main__":
    elements = [1, 2, 3]
    all_perms = permute(elements)
    print(f"Permutations of {elements} (Total: {len(all_perms)}):")
    for p in all_perms:
        print(p)