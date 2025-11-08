# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('titanic')


print("First 5 rows:")
print(df.head())
print("\nLast 5 rows:")
print(df.tail())

print(f"\nNumber of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")

print("\nColumn names and data types:")
print(df.dtypes)

print("\n.info() output:")
print(df.info())
print("\n.describe() output:")
print(df.describe())

# datawrangler install in vscode 


