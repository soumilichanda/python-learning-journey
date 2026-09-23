def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    result: list[list[int]] = []
    path: list[int] = []

    def backtrack(remain: int, start_idx: int) -> None:
        if remain == 0:
            result.append(list(path))
            return
        if remain < 0:
            return  # Prune branch: exceeded target

        for i in range(start_idx, len(candidates)):
            path.append(candidates[i])
            # Element reuse permitted: recurse with same index i
            backtrack(remain - candidates[i], i)
            path.pop()

    backtrack(target, 0)
    return result


if __name__ == "__main__":
    nums = [2, 3, 6, 7]
    target_val = 7
    combinations = combination_sum(nums, target_val)
    print(f"Combinations summing to {target_val} from {nums}:")
    print(combinations)