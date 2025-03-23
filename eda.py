import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_excel("first_15_rows(2).xlsx", engine="openpyxl")

# Preview the dataset
print("First 5 rows:")
print(df.head())

# Basic info
print("\nDataset Info:")
print(df.info())

# Describe numeric columns
print("\nSummary Statistics:")
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Class distribution
print("\nClass Distribution:")
print(df["Label"].value_counts())

# Drop non-numeric for correlation analysis
df_numeric = df.drop(columns=["Flow ID", "Src IP", "Dst IP", "Timestamp"], errors='ignore')

# Correlation heatmap
plt.figure(figsize=(12, 10))
corr = df_numeric.corr()
sns.heatmap(corr, cmap="coolwarm", center=0)
plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.show()

# Boxplot for a few features
features_to_plot = ["Flow Duration", "Total Fwd Packet", "Total Bwd packets", "Flow Bytes/s"]

for feature in features_to_plot:
    plt.figure(figsize=(6, 4))
    sns.boxplot(data=df, x="Label", y=feature)
    plt.title(f"{feature} vs Label")
    plt.tight_layout()
    plt.savefig(f"{feature}_boxplot.png")
    plt.show()