import pandas as pd

try:
    df = pd.read_excel("cocktails.xlsx")
    print("Excel file read successfully.")
    print("Columns:", df.columns.tolist())
    print("First 5 rows:\n", df.head())
except FileNotFoundError:
    print("Error: cocktails.xlsx not found. Make sure it's in the root directory.")
except Exception as e:
    print(f"Error reading Excel file: {e}")
