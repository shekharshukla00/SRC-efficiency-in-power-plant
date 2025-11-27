import pandas as pd

# Load data
df = pd.read_csv("SCR_Efficiency_Final_Cleaned.csv")

# Create engineered features
df["NOx_Diff"] = df["Inlet NOx (mg/m³)"] - df["NOx Emission (mg/m³)"]
df["NOx_per_NH3"] = df["Inlet NOx (mg/m³)"] / df["NH₃ Flow (kg/h)"]

# Update condition to be more flexible
df["Maintenance_Required"] = (df["NOx_Diff"] < 8) & (df["NOx_per_NH3"] > 65)

# Check how many rows qualify
print("Rows needing maintenance:", df["Maintenance_Required"].sum())

# Balanced sampling
maintenance_cases = df[df["Maintenance_Required"] == True]
healthy_cases = df[df["Maintenance_Required"] == False]

# Safe sampling
maintenance_sample = maintenance_cases.sample(min(5, maintenance_cases.shape[0]), random_state=1)
healthy_sample = healthy_cases.sample(min(5, healthy_cases.shape[0]), random_state=2)

# Combine and save
test_cases = pd.concat([maintenance_sample, healthy_sample])
test_cases.to_csv("SCR_Test_Cases.csv", index=False)
print("✅ Sample test cases saved to SCR_Test_Cases.csv")
