import pandas as pd

if __name__ == "__main__":
    data = {
        "EmployeeID": [101, 102, 103, 104, 105],
        "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
        "Department": ["IT", "HR", "IT", "Finance", "IT"],
        "Salary": [75000, 50000, 82000, 65000, 68000],
        "Experience": [3, 2, 5, 4, 1],
    }
    df = pd.DataFrame(data)

    # 1. Boolean condition filtering
    it_high_salary = df[(df["Department"] == "IT") & (df["Salary"] > 70000)]
    print("IT staff with salary > 70k:\n", it_high_salary)

    # 2. Label-based selection via .loc
    loc_selection = df.loc[df["Salary"] > 70000, ["Name", "Salary"]]
    print("\n.loc selection:\n", loc_selection)

    # 3. Position-based selection via .iloc (rows 1:4, first 2 cols)
    iloc_selection = df.iloc[1:4, :2]
    print("\n.iloc selection:\n", iloc_selection)