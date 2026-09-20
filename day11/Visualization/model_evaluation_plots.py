import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
    epochs = np.arange(1, 21)
    
    train_loss = 0.8 * np.exp(-0.15 * epochs) + np.random.normal(0, 0.015, size=20)
    val_loss = 0.85 * np.exp(-0.12 * epochs) + np.random.normal(0, 0.02, size=20)
    val_loss[14:] += np.linspace(0.01, 0.08, 6)

    cm = np.array([[430, 70],
                   [45, 455]])
    cm_normalized = cm.astype("float") / cm.sum(axis=1)[:, np.newaxis]

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # 1. Loss Curves
    axes[0].plot(epochs, train_loss, label="Training Loss", color="teal", linewidth=2)
    axes[0].plot(epochs, val_loss, label="Validation Loss", color="crimson", linestyle="--", linewidth=2)
    axes[0].set_title("Training vs Validation Loss Over Epochs")
    axes[0].set_xlabel("Epoch")
    axes[0].set_ylabel("Loss")
    axes[0].legend()
    axes[0].grid(True, linestyle=":", alpha=0.6)

    # 2. Confusion Matrix Heatmap
    labels = ["Cat", "Dog"]
    sns.heatmap(cm_normalized, annot=True, fmt=".2%", cmap="Blues", ax=axes[1],
                xticklabels=labels, yticklabels=labels)
    axes[1].set_title("Normalized Confusion Matrix")
    axes[1].set_xlabel("Predicted Label")
    axes[1].set_ylabel("True Label")

    plt.tight_layout()
    plt.savefig("evaluation_metrics.png", dpi=300)
    print("Saved evaluation_metrics.png successfully.")
    plt.show()