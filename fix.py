import pandas as pd

# Load the CSV file
df = pd.read_csv("Scenarios2.csv", sep=';')

# Replace 'M' with 'T' in the ThreatID column
df['ThreatID'] = df['ThreatID'].str.replace('^M', 'T', regex=True)

# Save the updated CSV
df.to_csv("updated_file.csv", index=False, sep=';')