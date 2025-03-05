from quantalogic.tools import PythonTool

# Initialize the tool
python_tool = PythonTool()

# Define a Python script to read and summarize the dataset
script_code = """
import pandas as pd
# Use the correct path inside the Docker container
# The host_dir parameter mounts your local ./data to /usr/src/host_data in the container
df = pd.read_excel('/usr/src/host_data/online+retail.xlsx')
summary = df.describe(include='all')
print(summary)
"""

# Execute the script inside QuantaLogic's PythonTool
output = python_tool.execute(
    install_commands="pip install pandas openpyxl",
    script=script_code,
    version="3.12",
    host_dir="./data",  # This mounts your local ./data to /usr/src/host_data in the container
    memory_limit="1g",
    environment_vars={}
)

# Print the output
print("Script Output:", output)