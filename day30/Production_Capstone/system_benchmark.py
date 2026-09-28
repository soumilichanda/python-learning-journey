import time
from inference_cache import LRUInferenceCache


def mock_model_inference(features: tuple[float, ...]) -> dict:
    # Simulated computation overhead
    time.sleep(0.001)
    score = sum(features)
    prob = 1.0 / (1.0 + (2.71828 ** (-score)))
    return {"prediction": 1 if prob >= 0.5 else 0, "probability": round(prob, 4)}


def run_benchmark(iterations: int = 500):
    cache = LRUInferenceCache(capacity=64)

    test_vectors = [
        (0.5, -1.2, 0.8, 2.1),
        (1.1, 0.4, -0.3, 0.9),
        (0.5, -1.2, 0.8, 2.1),  # Repeated query (Cache Hit)
        (-0.8, -0.5, 0.2, 0.1),
        (1.1, 0.4, -0.3, 0.9),  # Repeated query (Cache Hit)
    ]

    start_time = time.perf_counter()

    for i in range(iterations):
        vec = test_vectors[i % len(test_vectors)]
        cached_res = cache.get(vec)
        if cached_res is None:
            res = mock_model_inference(vec)
            cache.put(vec, res)

    total_time_ms = (time.perf_counter() - start_time) * 1000.0
    avg_latency = total_time_ms / iterations
    qps = iterations / (total_time_ms / 1000.0)

    print("=== Milestone 5: System Benchmark & Performance Report ===")
    print(f"Total Requests Simulated : {iterations}")
    print(f"Total Execution Time     : {total_time_ms:.2f} ms")
    print(f"Average Request Latency  : {avg_latency:.3f} ms")
    print(f"Throughput (QPS)         : {qps:.1f} req/sec")
    print("Cache Telemetry          :", cache.stats())


if __name__ == "__main__":
    run_benchmark(iterations=1000)