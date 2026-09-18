import pandas as pd

if __name__ == "__main__":
    # 1. Pandas Series with custom index
    marks = [88, 92, 79, 95]
    students = ["Alice", "Bob", "Charlie", "Diana"]
    student_series = pd.Series(marks, index=students, name="Scores")
    print("Series:\n", student_series)
    print("\nAlice's score:", student_series.loc["Alice"])

    # 2. DataFrame from dictionary
    data = {
        "Name": ["Alice", "Bob", "Charlie", "Diana"],
        "Age": [20, 21, 19, 22],
        "Grade": ["A", "A", "B", "A+"],
        "City": ["New York", "Chicago", "Boston", "Seattle"]
    }
    df = pd.DataFrame(data)
    print("\nDataFrame:\n", df)

    # 3. Column access as Series
    grades_col = df["Grade"]
    print("\nExtracted Column (Series):\n", grades_col)