from pathlib import Path
import pandas as pd

RAW_DATA = Path("data/raw")

print("=" * 80)
print("DATA INGESTION REPORT")
print("=" * 80)

for file in sorted(RAW_DATA.glob("*.csv")):

    print("\n")
    print("=" * 80)
    print(f"FILE: {file.name}")
    print("=" * 80)

    try:
        df = pd.read_csv(file)

        print("\nShape:")
        print(df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nHead:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"ERROR READING {file.name}: {e}")