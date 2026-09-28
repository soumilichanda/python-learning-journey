import time
from collections import defaultdict


class TelemetryLogger:
    def __init__(self):
        self.request_count = 0
        self.total_latency_ms = 0.0
        self.status_codes = defaultdict(int)

    def log_inference(self, latency_ms: float, status_code: int = 200):
        self.request_count += 1
        self.total_latency_ms += latency_ms
        self.status_codes[status_code] += 1

    def get_metrics(self) -> dict:
        avg_latency = (
            (self.total_latency_ms / self.request_count)
            if self.request_count > 0
            else 0.0
        )
        return {
            "total_requests": self.request_count,
            "avg_latency_ms": round(avg_latency, 3),
            "status_distribution": dict(self.status_codes),
        }