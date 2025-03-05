# Use for Loading the Data from the Data Source

import pandas as pd

# Load dataset
file_path = "./data/online+retail.xlsx"
df = pd.read_excel(file_path)

# Display basic information about the dataset
print(df.info())
print(df.head())