def group_anagrams(strs: list[str]) -> list[list[str]]:
    grouped: dict[tuple[int, ...], list[str]] = {}

    for s in strs:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord("a")] += 1
        key = tuple(count)
        grouped.setdefault(key, []).append(s)

    return list(grouped.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print("Grouped Anagrams:", group_anagrams(strs))