# Call the PythonTool
from quantalogic.tools import PythonTool
python_tool = PythonTool()

# Define the script to be executed
script_code = """
import pandas as pd

# Read dataset
file_path = '/usr/src/host_data/online+retail.xlsx'
df = pd.read_excel(file_path)

# Top 10 best-selling products
top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
print("Top-Selling Products:\\n", top_products)
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