import time
import numpy as np


class InferenceService:
    """Simulates an interactive serving engine with preprocessing and decision confidence."""

    def __init__(self, threshold: float = 0.5):
        self.threshold = threshold
        # Synthetic weights representing a trained classifier
        self.weights = np.array([0.75, -0.45, 1.20], dtype=np.float32)
        self.bias = -0.15

    def predict(self, feature_1: float, feature_2: float, feature_3: float) -> dict[str, float | str]:
        start_time = time.perf_counter()

        x = np.array([feature_1, feature_2, feature_3], dtype=np.float32)
        logit = float(np.dot(x, self.weights) + self.bias)
        probability = 1.0 / (1.0 + np.exp(-logit))  # Sigmoid activation

        label = "Positive" if probability >= self.threshold else "Negative"
        latency_ms = (time.perf_counter() - start_time) * 1000

        return {
            "prediction": label,
            "confidence": round(probability if label == "Positive" else 1 - probability, 4),
            "latency_ms": round(latency_ms, 3),
        }


def launch_mock_ui():
    engine = InferenceService(threshold=0.5)
    sample_inputs = [
        (1.2, 0.4, -0.8),
        (2.5, -1.0, 1.5),
        (-0.5, 2.0, -1.2),
    ]

    print("=== Model Serving Inference Simulation ===")
    for idx, (f1, f2, f3) in enumerate(sample_inputs, 1):
        result = engine.predict(f1, f2, f3)
        print(f"Sample {idx}: Features=({f1}, {f2}, {f3}) -> Label: {result['prediction']} | "
              f"Confidence: {result['confidence'] * 100:.1f}% | Latency: {result['latency_ms']} ms")


if __name__ == "__main__":
    launch_mock_ui()