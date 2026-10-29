
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

import pandas as pd

# Create a sample customer churn dataset
data = {
    "CustomerID": list(range(1, 21)),
    "Gender": [
        "Male", "Female", "Male", "Female", "Male",
        "Female", "Male", "Female", "Male", "Female",
        "Male", "Female", "Male", "Female", "Male",
        "Female", "Male", "Female", "Male", "Female"
    ],
    "Tenure": [
        1, 12, 24, 36, 6, 48, 60, 3, 18, 30,
        42, 9, 55, 15, 27, 33, 5, 50, 20, 40
    ],
    "MonthlyCharges": [
        80, 60, 90, 75, 95, 55, 45, 100, 70, 65,
        85, 110, 50, 72, 88, 68, 120, 58, 78, 82
    ],
    "TotalCharges": [
        80, 720, 2160, 2700, 570, 2640, 2700, 300,
        1260, 1950, 3570, 990, 2750, 1080, 2376,
        2244, 600, 2900, 1560, 3280
    ],
    "Contract": [
        "Month-to-month", "One year", "Two year", "One year",
        "Month-to-month", "Two year", "Two year", "Month-to-month",
        "One year", "Month-to-month", "Two year", "Month-to-month",
        "Two year", "One year", "Month-to-month", "One year",
        "Month-to-month", "Two year", "One year", "Two year"
    ],
    "Churn": [
        "Yes", "No", "No", "No", "Yes", "No", "No", "Yes",
        "No", "Yes", "No", "Yes", "No", "No", "Yes",
        "No", "Yes", "No", "No", "No"
    ]
}

df = pd.DataFrame(data)

# Save the dataset as a CSV file
df.to_csv("customer_churn.csv", index=False)

print("Customer churn dataset created successfully!")
print(df.head())

# 1. Load the dataset
df = pd.read_csv("customer_churn.csv")

# 2. Display dataset details
print("First five records:")
print(df.head())

print("\nDataset information:")
df.info()

print("\nColumn names:")
print(df.columns.tolist())

# 3. Descriptive statistics
numeric_df = df.select_dtypes(include=np.number)

print("\nMean:\n", numeric_df.mean())
print("\nMedian:\n", numeric_df.median())
print("\nMode:\n", df.mode().iloc[0])
print("\nStandard deviation:\n", numeric_df.std())
print("\nVariance:\n", numeric_df.var())
print("\nMinimum:\n", numeric_df.min())
print("\nMaximum:\n", numeric_df.max())
print("\nPercentiles:\n", numeric_df.quantile([0.25, 0.50, 0.75]))

# 4. Data visualization
if not numeric_df.empty:
    col = numeric_df.columns[0]

    # Histogram
    sns.histplot(data=df, x=col, kde=True)
    plt.title("Histogram")
    plt.show()

    # Box plot
    sns.boxplot(data=df, x=col)
    plt.title("Box Plot")
    plt.show()

    # Scatter plot
    if len(numeric_df.columns) >= 2:
        sns.scatterplot(
            data=df,
            x=numeric_df.columns[0],
            y=numeric_df.columns[1]
        )
        plt.title("Scatter Plot")
        plt.show()

    # Correlation heatmap
    plt.figure(figsize=(10, 6))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()

# 5. Handle missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

clean_df = df.copy()

# Replace missing numerical values with column means
for col in clean_df.select_dtypes(include=np.number).columns:
    clean_df[col] = clean_df[col].fillna(clean_df[col].mean())

# Remove rows with remaining missing values
clean_df = clean_df.dropna()

print("\nMissing values after cleaning:")
print(clean_df.isnull().sum())

# 6. Detect and cap outliers using Z-score limits
numeric_cols = clean_df.select_dtypes(include=np.number).columns
variable_cols = [
    col for col in numeric_cols
    if clean_df[col].nunique() > 1
]

if variable_cols and len(clean_df) > 1:
    z_scores = clean_df[variable_cols].apply(
        lambda col: zscore(col, nan_policy="omit")
    )

    outlier_rows = z_scores.abs().gt(3).any(axis=1)

    print("\nPotential outlier records:")
    print(clean_df.loc[outlier_rows])

    # Cap values outside mean +/- 3 standard deviations
    for col in variable_cols:
        mean = clean_df[col].mean()
        std = clean_df[col].std(ddof=0)

        clean_df[col] = clean_df[col].clip(
            lower=mean - 3 * std,
            upper=mean + 3 * std
        )

# 7. Verify cleaned data
print("\nFinal dataset:")
print(clean_df.head())

print("\nRemaining missing values:")
print(clean_df.isnull().sum())

print("\nFinal dataset shape:", clean_df.shape)

# 8. Save cleaned dataset
clean_df.to_csv("customer_churn_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")
