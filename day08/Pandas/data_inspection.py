import pandas as pd

if __name__ == "__main__":
    records = {
        "TransactionID": range(101, 111),
        "User": ["U1", "U2", "U3", "U4", "U5", "U6", "U7", "U8", "U9", "U10"],
        "Amount": [250.0, 15.5, 89.9, 1200.0, 45.0, 310.2, 75.0, 890.5, 23.0, 110.0],
        "ItemsCount": [3, 1, 2, 8, 1, 4, 2, 6, 1, 2]
    }
    df = pd.DataFrame(records)

    # 1. Top and bottom records
    print("Top 3 rows:\n", df.head(3))
    print("\nBottom 2 rows:\n", df.tail(2))

    # 2. Shape, column list, and types
    print("\nDataset Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print("\nData Types:\n", df.dtypes)

    # 3. Structural info and numeric distribution
    print("\nInfo:")
    df.info()

    print("\nDescriptive Statistics:\n", df.describe())