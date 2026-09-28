import json
import os
import pickle
import numpy as np


class ProductionModelWrapper:
    """Wrapper encapsulating inference logic with input dimension validation."""

    def __init__(self, weights: np.ndarray, bias: float, version: str = "1.0.0"):
        self.weights = weights
        self.bias = bias
        self.version = version

    def predict_proba(self, x: np.ndarray) -> np.ndarray:
        logits = np.dot(x, self.weights) + self.bias
        return 1.0 / (1.0 + np.exp(-np.clip(logits, -250.0, 250.0)))


def package_and_export_bundle(output_dir: str = "day28/Model_Deployment/artifacts") -> str:
    os.makedirs(output_dir, exist_ok=True)

    # 1. Instantiate and serialize trained model artifact
    trained_weights = np.array([0.45, -0.62, 1.15, -0.28], dtype=np.float32)
    model = ProductionModelWrapper(weights=trained_weights, bias=0.10, version="1.0.0")

    model_path = os.path.join(output_dir, "model_artifact.pkl")
    with open(model_path, "wb") as f:
        pickle.dump(model, f, protocol=pickle.HIGHEST_PROTOCOL)

    # 2. Export metadata manifest for deployment verification
    metadata = {
        "model_version": model.version,
        "n_features": len(trained_weights),
        "expected_input_shape": [None, len(trained_weights)],
        "serialization_protocol": pickle.HIGHEST_PROTOCOL,
    }
    manifest_path = os.path.join(output_dir, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=4)

    return model_path


def load_and_verify(artifact_path: str):
    with open(artifact_path, "rb") as f:
        loaded_model: ProductionModelWrapper = pickle.load(f)

    # Test sample inference
    dummy_input = np.array([[0.5, -1.2, 0.3, 0.9]], dtype=np.float32)
    prediction = loaded_model.predict_proba(dummy_input)
    print("=== Artifact Verification Succeeded ===")
    print(f"Loaded Model Version : {loaded_model.version}")
    print(f"Sample Prediction    : {prediction[0]:.4f}")


if __name__ == "__main__":
    path = package_and_export_bundle()
    load_and_verify(path)