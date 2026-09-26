from collections import Counter
import heapq


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    count_map = Counter(nums)
    # Min-heap stores tuples of (frequency, value)
    min_heap: list[tuple[int, int]] = []

    for val, freq in count_map.items():
        heapq.heappush(min_heap, (freq, val))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return [val for freq, val in min_heap]


if __name__ == "__main__":
    nums_arr = [1, 1, 1, 2, 2, 3]
    k_val = 2
    frequent_items = top_k_frequent(nums_arr, k_val)
    print("=== Top K Frequent Elements ===")
    print(f"Array: {nums_arr}, k={k_val} -> {frequent_items} (Expected: [2, 1] or [1, 2])")