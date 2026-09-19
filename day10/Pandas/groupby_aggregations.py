import pandas as pd

if __name__ == "__main__":
    data = {
        "Category": ["Tech", "Tech", "Home", "Home", "Tech", "Home"],
        "CustomerSegment": ["Corp", "Consumer", "Corp", "Consumer", "Corp", "Corp"],
        "Amount": [1200.0, 450.0, 300.0, 150.0, 950.0, 700.0],
        "Rating": [4.8, 4.2, 4.5, 3.8, 4.9, 4.1],
    }
    df = pd.DataFrame(data)

    # 1. Multi-metric column aggregation
    agg_metrics = df.groupby("Category").agg(
        total_amount=("Amount", "sum"),
        avg_amount=("Amount", "mean"),
        avg_rating=("Rating", "mean"),
    )
    print("Aggregated metrics by Category:\n", agg_metrics)

    # 2. Multi-column grouping
    multi_group = df.groupby(["Category", "CustomerSegment"])["Amount"].mean()
    print("\nMean Amount by Category and Segment:\n", multi_group)

    # 3. Add group-level benchmark back using transform
    df["CategoryAvgSpend"] = df.groupby("Category")["Amount"].transform("mean")
    print("\nDataFrame with group transform column:\n", df)