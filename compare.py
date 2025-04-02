import pandas as pd

# Load both files
file1 = pd.read_csv('scenarios2.1.csv', sep=';')
file2 = pd.read_csv('updated_file.csv', sep=';')

# Normalize column names (remove spaces etc.)
file1.columns = file1.columns.str.strip()
file2.columns = file2.columns.str.strip()

# Find common rows
common_rows = pd.merge(file1, file2, on=['ScenarioID', 'ThreatID', 'VulnID'])

# Show common rows
print("Exact matches:")
print(common_rows)