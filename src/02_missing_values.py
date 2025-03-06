# Call the PythonTool
from quantalogic.tools import PythonTool
python_tool = PythonTool()

# Define the script to be executed
script_code = """
import pandas as pd

# Read dataset
file_path = '/usr/src/host_data/online+retail.xlsx'
df = pd.read_excel(file_path)

# Count missing values
missing_summary = df.isnull().sum()
print("Missing Values:\\n", missing_summary)

# Fill missing CustomerID with -1 (anonymous)
df['CustomerID'].fillna(-1, inplace=True)

# Fill missing descriptions with 'Unknown'
df['Description'].fillna('Unknown', inplace=True)

# Confirm changes
print("Missing Values After Fix:\\n", df.isnull().sum())
"""

# Execute the script
output = python_tool.execute(
    install_commands="pip install pandas openpyxl",
    script=script_code,
    version="3.12",
    host_dir="./data",
    memory_limit="1g",
    environment_vars={}
)

# Print the output
print("Script Output:", output)