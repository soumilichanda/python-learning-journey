def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    counts: dict[str, int] = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1

    for char in t:
        if char not in counts or counts[char] == 0:
            return False
        counts[char] -= 1

    return True


if __name__ == "__main__":
    s, t = "anagram", "nagaram"
    print(f"'{s}' and '{t}' are anagrams:", is_anagram(s, t))
    print(f"'rat' and 'car' are anagrams:", is_anagram("rat", "car"))