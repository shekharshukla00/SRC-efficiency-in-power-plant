import pandas as pd

# Define test cases as a list of dicts
test_inputs = [
    {
        "Boiler Load (MW)": 740.0, "Inlet NOx (mg/m³)": 310.0, "Inlet O₂ (%)": 4.3,
        "Flue Gas Flow (m³/h)": 68.5, "NH₃ Flow (kg/h)": 4.2, "Flue Gas Temp (°C)": 358.0,
        "Coal Feed Rate (t/h)": 1350.0, "Case": "✅ Normal"
    },
    {
        "Boiler Load (MW)": 700.0, "Inlet NOx (mg/m³)": 340.0, "Inlet O₂ (%)": 4.5,
        "Flue Gas Flow (m³/h)": 67.0, "NH₃ Flow (kg/h)": 4.0, "Flue Gas Temp (°C)": 360.0,
        "Coal Feed Rate (t/h)": 1300.0, "Case": "⚠️ High NH₃ usage"
    },
    {
        "Boiler Load (MW)": 750.0, "Inlet NOx (mg/m³)": 320.0, "Inlet O₂ (%)": 4.4,
        "Flue Gas Flow (m³/h)": 70.0, "NH₃ Flow (kg/h)": 4.1, "Flue Gas Temp (°C)": 355.0,
        "Coal Feed Rate (t/h)": 1320.0, "Case": "🔻 Low Efficiency"
    },
    {
        "Boiler Load (MW)": 695.0, "Inlet NOx (mg/m³)": 330.0, "Inlet O₂ (%)": 4.6,
        "Flue Gas Flow (m³/h)": 66.5, "NH₃ Flow (kg/h)": 3.9, "Flue Gas Temp (°C)": 357.0,
        "Coal Feed Rate (t/h)": 1270.0, "Case": "🛠 Both Triggers"
    },
    {
        "Boiler Load (MW)": 770.0, "Inlet NOx (mg/m³)": 300.0, "Inlet O₂ (%)": 4.2,
        "Flue Gas Flow (m³/h)": 69.5, "NH₃ Flow (kg/h)": 4.3, "Flue Gas Temp (°C)": 359.0,
        "Coal Feed Rate (t/h)": 1400.0, "Case": "✅ High Efficiency"
    },
    {
        "Boiler Load (MW)": 680.0, "Inlet NOx (mg/m³)": 270.0, "Inlet O₂ (%)": 4.1,
        "Flue Gas Flow (m³/h)": 66.8, "NH₃ Flow (kg/h)": 3.6, "Flue Gas Temp (°C)": 352.0,
        "Coal Feed Rate (t/h)": 1250.0, "Case": "✅ Low Load/Idle"
    }
]

# Convert to DataFrame
test_df = pd.DataFrame(test_inputs)

# Save to CSV
csv_path = "SCR_Test_Inputs.csv"
test_df.to_csv(csv_path, index=False)

csv_path
