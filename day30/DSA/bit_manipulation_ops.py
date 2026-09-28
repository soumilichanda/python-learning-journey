def single_number(nums: list[int]) -> int:
    unique = 0
    for x in nums:
        unique ^= x
    return unique


def hamming_weight(n: int) -> int:
    count = 0
    while n:
        n &= n - 1  # Clears the lowest set bit
        count += 1
    return count


if __name__ == "__main__":
    sample_nums = [4, 1, 2, 1, 2]
    val = single_number(sample_nums)
    print("=== Bit Manipulation Invariants ===")
    print(f"Array: {sample_nums} -> Unique element: {val} (Expected: 4)")

    bit_pattern = 29  # Binary: 11101 -> 4 bits set
    set_bits = hamming_weight(bit_pattern)
    print(f"Number: {bit_pattern} (bin: {bin(bit_pattern)}) -> Set Bits: {set_bits} (Expected: 4)")