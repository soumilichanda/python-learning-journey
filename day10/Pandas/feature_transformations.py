import pandas as pd

if __name__ == "__main__":
    data = {
        "CustomerID": ["C-101", "C-102", "C-103", "C-104", "C-105"],
        "Age": [19, 34, 45, 28, 62],
        "Email": ["alok@gmail.com", "bristi@yahoo.com", "charulata@corp.net", "dinesh@gmail.com", "era@corp.net"],
        "Tier": ["Silver", "Gold", "Bronze", "Silver", "Platinum"],
    }
    df = pd.DataFrame(data)

    # 1. Continuous binning into categories
    age_bins = [0, 25, 45, 100]
    age_labels = ["Young", "Adult", "Senior"]
    df["AgeGroup"] = pd.cut(df["Age"], bins=age_bins, labels=age_labels)

    # 2. String accessor transformations
    df["EmailDomain"] = df["Email"].str.split("@").str[1]
    df["DomainName"] = df["EmailDomain"].str.split(".").str[0].str.upper()

    # 3. Categorical encoding mapping
    tier_weights = {"Bronze": 1, "Silver": 2, "Gold": 3, "Platinum": 4}
    df["TierRank"] = df["Tier"].map(tier_weights)

    # 4. Indicator flag
    df["IsCorpDomain"] = df["EmailDomain"] == "corp.net"

    print("Transformed Feature Set:\n", df[["CustomerID", "AgeGroup", "DomainName", "TierRank", "IsCorpDomain"]])