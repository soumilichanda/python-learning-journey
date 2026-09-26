import heapq


def find_kth_largest(nums: list[int], k: int) -> int:
    # Maintain a min-heap with a maximum capacity of k
    min_heap: list[int] = []

    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # The root of the min-heap holds the kth largest element
    return min_heap[0]


if __name__ == "__main__":
    sample_nums = [3, 2, 1, 5, 6, 4]
    k_target = 2
    res = find_kth_largest(sample_nums, k_target)
    print("=== Find Kth Largest Element via Min-Heap ===")
    print(f"Array: {sample_nums}, k={k_target} -> {res} (Expected: 5)")