import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
    np.random.seed(42)

    spending = np.concatenate([
        np.random.normal(loc=120, scale=30, size=800),
        np.random.exponential(scale=150, size=150),
        [650, 720, 810, 950]
    ])

    df = pd.DataFrame({"CustomerSpending": spending})

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # 1. Histogram with KDE
    sns.histplot(df["CustomerSpending"], kde=True, ax=axes[0], color="royalblue", bins=30)
    axes[0].set_title("Customer Spending Distribution (Histogram + KDE)")
    axes[0].set_xlabel("Spending ($)")
    axes[0].set_ylabel("Frequency")

    # 2. Boxplot for outlier detection
    sns.boxplot(x=df["CustomerSpending"], ax=axes[1], color="salmon")
    axes[1].set_title("Outlier Detection (Boxplot)")
    axes[1].set_xlabel("Spending ($)")

    plt.tight_layout()
    plt.savefig("distribution_analysis.png", dpi=300)
    print("Saved distribution_analysis.png successfully.")
    plt.show()