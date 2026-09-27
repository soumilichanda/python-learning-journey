import numpy as np


class BackboneClassifierPipeline:
    def __init__(self, feature_dim: int = 16, num_classes: int = 2):
        self.feature_dim = feature_dim
        # Trainable classification head parameters
        self.w_head = np.random.randn(feature_dim, num_classes) * 0.05
        self.b_head = np.zeros((1, num_classes))

    @staticmethod
    def frozen_feature_backbone(x: np.ndarray) -> np.ndarray:
        """Simulates frozen pre-trained CNN layers producing spatial pooled feature vectors."""
        # Fixed deterministic weights representing frozen filters
        frozen_projection = np.linspace(-0.5, 0.5, num=x.size).reshape(x.shape)
        filtered = np.maximum(0.0, x * frozen_projection)
        # Global Average Pooling across spatial dimensions
        return np.mean(filtered, axis=(2, 3))  # Shape: (B, C)

    def forward(self, batch_images: np.ndarray) -> np.ndarray:
        # 1. Feature extraction through frozen backbone
        features = self.frozen_feature_backbone(batch_images)
        # 2. Linear classification forward pass
        logits = np.dot(features, self.w_head) + self.b_head
        # 3. Stable Softmax probability computation
        exp_logits = np.exp(logits - np.max(logits, axis=1, keepdims=True))
        return exp_logits / np.sum(exp_logits, axis=1, keepdims=True)


if __name__ == "__main__":
    np.random.seed(42)
    # Batch of 4 images: (Batch=4, Channels=16, H=8, W=8)
    batch = np.random.randn(4, 16, 8, 8)

    model = BackboneClassifierPipeline(feature_dim=16, num_classes=2)
    probs = model.forward(batch)

    print("=== Transfer Learning Backbone Simulation ===")
    print(f"Input Batch Shape  : {batch.shape}")
    print(f"Class Probabilities:\n{probs}")
    print(f"Sum of Probs (Row 1): {np.sum(probs[0]):.4f} (Expected: 1.0)")