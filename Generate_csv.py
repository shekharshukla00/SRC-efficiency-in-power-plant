import pandas as pd

# Load filtered SCR data
file_path = "SCR_SelectData2100_8Variables_Outlier_filter.txt"
df = pd.read_csv(file_path, sep=r'\s+', header=None, engine='python')

# Assign proper column names based on official README
df.columns = [
    "Boiler Load (MW)",
    "Inlet NOx (mg/m³)",
    "Inlet O₂ (%)",
    "Flue Gas Flow (km³/h)",
    "NH₃ Flow (kg/h)",
    "Flue Gas Temp (°C)",
    "Coal Feed Rate (t/h)",
    "NOx Emission (mg/m³)"
]

# Save the cleaned data to CSV
output_path = "SCR_Efficiency_Final_Cleaned.csv"
df.to_csv(output_path, index=False)
print(f"✅ Final dataset saved as {output_path}")
