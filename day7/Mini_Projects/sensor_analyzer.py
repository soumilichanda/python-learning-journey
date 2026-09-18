import time
import numpy as np

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def linear_search(arr, target):
    for idx, val in enumerate(arr):
        if val == target:
            return idx
    return -1

def generate_sensor_stream(size=50000):
    np.random.seed(42)
    raw = np.round(np.random.normal(loc=25.0, scale=3.0, size=size), 1)
    
    # Inject missing flags (-999.0) and extreme spikes
    raw[np.random.choice(size, size=size // 50, replace=False)] = -999.0
    raw[np.random.choice(size, size=size // 100, replace=False)] = 250.0
    return raw

def clean_and_impute(stream):
    valid_mask = (stream != -999.0) & (stream <= 100.0)
    valid_data = stream[valid_mask]
    impute_mean = round(float(np.mean(valid_data)), 1)
    
    # Impute missing records with the computed valid mean
    cleaned = np.where(stream == -999.0, impute_mean, stream)
    # Filter out anomalous spikes
    return cleaned[cleaned <= 100.0]

def benchmark_search(sorted_data, query):
    t0 = time.perf_counter()
    lin_idx = linear_search(sorted_data, query)
    t_lin = time.perf_counter() - t0

    t0 = time.perf_counter()
    bin_idx = binary_search(sorted_data, query)
    t_bin = time.perf_counter() - t0

    return lin_idx, t_lin, bin_idx, t_bin

if __name__ == "__main__":
    print("=== Sensor Stream Processing Pipeline (Week 1 Mini-Project) ===")
    raw_stream = generate_sensor_stream(size=100000)
    print(f"Total Raw Records Ingested : {len(raw_stream)}")

    clean_stream = clean_and_impute(raw_stream)
    print(f"Valid Records Post-Cleaning: {len(clean_stream)}")
    print(f"Mean Signal Temperature     : {np.mean(clean_stream):.2f}°C")

    # Prepare for binary search
    sorted_stream = np.sort(clean_stream)
    query_val = 26.5

    lin_idx, t_lin, bin_idx, t_bin = benchmark_search(sorted_stream, query_val)

    print("\n--- Search Efficiency Benchmark ---")
    print(f"Target Query : {query_val}°C")
    print(f"Linear Search: Index {lin_idx} | Time: {t_lin:.6f}s")
    print(f"Binary Search: Index {bin_idx} | Time: {t_bin:.6f}s")
    if t_bin > 0:
        print(f"Speedup Factor: {t_lin / t_bin:.1f}x faster")