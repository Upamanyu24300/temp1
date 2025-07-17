# import pandas as pd
# from models import EmissionInput, EmissionOutput, EmissionRecord
# import os
# from datetime import datetime

# # Load emission factors from processed CSV
# df_factors = pd.read_csv("processed/emission_factors.csv")

# # Enforce proper datetime parsing with explicit format
# df_factors["start_date"] = pd.to_datetime(df_factors["start_date"], errors="coerce")
# df_factors["end_date"] = pd.to_datetime(df_factors["end_date"], errors="coerce")

# # Remove any rows with invalid dates
# df_factors = df_factors.dropna(subset=["start_date", "end_date"])

# print(f"📊 Loaded {len(df_factors)} emission factors")
# print(f"📅 Date range: {df_factors['start_date'].min()} to {df_factors['end_date'].max()}")

# def calculate_emissions(input_data: EmissionInput) -> EmissionOutput:
#     input_date = pd.to_datetime(input_data.date_of_activity)
    
#     print(f"🔍 Incoming input: {input_data}")
#     print(f"🔍 Input date: {input_date}")
#     print(f"🔍 Available materials: {df_factors['material'].unique()}")
#     print(f"🔍 Available units: {df_factors['unit'].unique()}")
#     print(f"🔍 Available locations: {df_factors['location'].unique()}")
    
#     # Clean and normalize the input data
#     material_clean = input_data.material.strip().lower()
#     unit_clean = input_data.unit.strip()
#     location_clean = input_data.location.strip().lower()
    
#     print(f"🧹 Cleaned input - Material: '{material_clean}', Unit: '{unit_clean}', Location: '{location_clean}'")
    
#     # Create a copy of df_factors with normalized strings for matching
#     df_normalized = df_factors.copy()
#     df_normalized['material_norm'] = df_normalized['material'].astype(str).str.strip().str.lower()
#     df_normalized['unit_norm'] = df_normalized['unit'].astype(str).str.strip()
#     df_normalized['location_norm'] = df_normalized['location'].astype(str).str.strip().str.lower()
    
#     # Debug: Show what we're trying to match
#     print(f"🔍 Looking for matches where:")
#     print(f"   - Material: '{material_clean}' in {df_normalized['material_norm'].unique()}")
#     print(f"   - Unit: '{unit_clean}' in {df_normalized['unit_norm'].unique()}")
#     print(f"   - Location: '{location_clean}' in {df_normalized['location_norm'].unique()}")
#     print(f"   - Date: {input_date} between start_date and end_date")
    
#     # Filter step by step for debugging
#     material_matches = df_normalized[df_normalized['material_norm'] == material_clean]
#     print(f"🔍 Material matches: {len(material_matches)}")
    
#     unit_matches = material_matches[material_matches['unit_norm'] == unit_clean]
#     print(f"🔍 Unit matches: {len(unit_matches)}")
    
#     location_matches = unit_matches[unit_matches['location_norm'] == location_clean]
#     print(f"🔍 Location matches: {len(location_matches)}")
    
#     date_matches = location_matches[
#         (location_matches['start_date'] <= input_date) & 
#         (location_matches['end_date'] >= input_date)
#     ]
#     print(f"🔍 Date matches: {len(date_matches)}")
    
#     if len(date_matches) == 0:
#         # Enhanced error message with debugging info
#         error_msg = f"No matching emission factor found for:\n"
#         error_msg += f"Material: '{input_data.material}' (normalized: '{material_clean}')\n"
#         error_msg += f"Unit: '{input_data.unit}' (normalized: '{unit_clean}')\n"
#         error_msg += f"Location: '{input_data.location}' (normalized: '{location_clean}')\n"
#         error_msg += f"Date: {input_data.date_of_activity} ({input_date})\n"
        
#         # Show available options
#         if len(material_matches) > 0:
#             error_msg += f"Available units for this material: {material_matches['unit_norm'].unique()}\n"
#         if len(unit_matches) > 0:
#             error_msg += f"Available locations for this material/unit: {unit_matches['location_norm'].unique()}\n"
#         if len(location_matches) > 0:
#             error_msg += f"Available date ranges for this combination:\n"
#             for _, row in location_matches.iterrows():
#                 error_msg += f"  - {row['start_date'].date()} to {row['end_date'].date()}\n"
        
#         raise ValueError(error_msg)
    
#     # Use the first match (you might want to add logic to handle multiple matches)
#     factor = date_matches.iloc[0]
#     emission = input_data.quantity * factor['value']
    
#     print(f"✅ Match found! Factor: {factor['value']}, Emission: {emission}")
    
#     return EmissionOutput(
#         emission_kg_co2e=round(emission, 3),
#         emission_factor_used=factor['value'],
#         factor_unit=factor['unit'],
#         factor_source=factor['source'],
#         valid_from=factor['start_date'].date(),
#         valid_to=factor['end_date'].date()
#     )

# def save_emission_record(record: EmissionRecord, file_path="processed/emission_records.csv"):
#     # Convert to dict
#     record_dict = record.model_dump()  # Use model_dump() instead of dict() for newer Pydantic versions
    
#     # Append or create new file
#     if os.path.exists(file_path):
#         df = pd.read_csv(file_path)
#         df = pd.concat([df, pd.DataFrame([record_dict])], ignore_index=True)
#     else:
#         df = pd.DataFrame([record_dict])
    
#     df.to_csv(file_path, index=False)
#     print(f"💾 Saved emission record to {file_path}")

# def get_yoy_emissions(file_path="processed/emission_records.csv") -> dict:
#     if not os.path.exists(file_path):
#         raise ValueError("No emission records found yet.")
    
#     df = pd.read_csv(file_path, parse_dates=["date_of_activity"])
#     df["year"] = df["date_of_activity"].dt.year
    
#     grouped = df.groupby("year")["emission_kg_co2e"].sum().to_dict()
    
#     current_year = max(grouped.keys(), default=None)
#     previous_year = current_year - 1 if current_year else None
    
#     result = {
#         "current_year": {
#             "scope1": round(grouped.get(current_year, 0), 2),
#             "scope2": 0
#         },
#         "previous_year": {
#             "scope1": round(grouped.get(previous_year, 0), 2),
#             "scope2": 0
#         }
#     }
    
#     prev = result["previous_year"]["scope1"]
#     curr = result["current_year"]["scope1"]
    
#     if prev > 0:
#         result["change_percentage"] = round(((curr - prev) / prev) * 100, 2)
#     else:
#         result["change_percentage"] = 100.0 if curr > 0 else 0.0
    
#     return result

# def get_emission_intensity(
#     records_path="processed/emission_records.csv",
#     metrics_path="processed/business_metrics.csv",
#     metric_name="Tons of Steel Produced"
# ) -> dict:
#     if not os.path.exists(records_path) or not os.path.exists(metrics_path):
#         raise ValueError("Required data files are missing.")
    
#     df_emissions = pd.read_csv(records_path, parse_dates=["date_of_activity"])
#     df_metrics = pd.read_csv(metrics_path, parse_dates=["date"])
    
#     # Group emissions monthly
#     df_emissions["month"] = df_emissions["date_of_activity"].dt.to_period("M")
#     monthly_emissions = df_emissions.groupby("month")["emission_kg_co2e"].sum()
    
#     # Group metrics monthly
#     df_metrics = df_metrics[df_metrics["metric_name"] == metric_name]
#     df_metrics["month"] = df_metrics["date"].dt.to_period("M")
#     monthly_metrics = df_metrics.groupby("month")["value"].sum()
    
#     # Align on month and calculate intensity
#     df_combined = pd.DataFrame({
#         "emissions": monthly_emissions,
#         "metric": monthly_metrics
#     }).dropna()
    
#     if len(df_combined) == 0:
#         return {}
    
#     df_combined["intensity"] = df_combined["emissions"] / df_combined["metric"]
#     df_combined = df_combined.reset_index()
    
#     # Output
#     return {
#         str(row["month"]): round(row["intensity"], 4)
#         for _, row in df_combined.iterrows()
#     }

# def get_emission_hotspot(file_path="processed/emission_records.csv") -> dict:
#     if not os.path.exists(file_path):
#         raise ValueError("No emission records found.")
    
#     df = pd.read_csv(file_path)
    
#     if "material" not in df.columns or "emission_kg_co2e" not in df.columns:
#         raise ValueError("Missing required columns.")
    
#     result = df.groupby("material")["emission_kg_co2e"].sum().sort_values(ascending=False)
#     return result.round(2).to_dict()

import pandas as pd
from models import EmissionInput, EmissionOutput, EmissionRecord
import os
from datetime import datetime

# Load emission factors from processed CSV
df_factors = pd.read_csv("processed/emission_factors.csv")

# Enforce proper datetime parsing with explicit format
df_factors["start_date"] = pd.to_datetime(df_factors["start_date"], errors="coerce")
df_factors["end_date"] = pd.to_datetime(df_factors["end_date"], errors="coerce")

# Remove any rows with invalid dates
df_factors = df_factors.dropna(subset=["start_date", "end_date"])

print(f"📊 Loaded {len(df_factors)} emission factors")
print(f"📅 Date range: {df_factors['start_date'].min()} to {df_factors['end_date'].max()}")

def calculate_emissions(input_data: EmissionInput) -> EmissionOutput:
    input_date = pd.to_datetime(input_data.date_of_activity)
    
    print(f"🔍 Incoming input: {input_data}")
    print(f"🔍 Input date: {input_date}")
    print(f"🔍 Available materials: {df_factors['material'].unique()}")
    print(f"🔍 Available units: {df_factors['unit'].unique()}")
    print(f"🔍 Available locations: {df_factors['location'].unique()}")
    
    # Clean and normalize the input data
    material_clean = input_data.material.strip().lower()
    unit_clean = input_data.unit.strip()
    location_clean = input_data.location.strip().lower()
    
    print(f"🧹 Cleaned input - Material: '{material_clean}', Unit: '{unit_clean}', Location: '{location_clean}'")
    
    # Create a copy of df_factors with normalized strings for matching
    df_normalized = df_factors.copy()
    df_normalized['material_norm'] = df_normalized['material'].astype(str).str.strip().str.lower()
    df_normalized['unit_norm'] = df_normalized['unit'].astype(str).str.strip()
    df_normalized['location_norm'] = df_normalized['location'].astype(str).str.strip().str.lower()
    
    # Debug: Show what we're trying to match
    print(f"🔍 Looking for matches where:")
    print(f"   - Material: '{material_clean}' in {df_normalized['material_norm'].unique()}")
    print(f"   - Unit: '{unit_clean}' in {df_normalized['unit_norm'].unique()}")
    print(f"   - Location: '{location_clean}' in {df_normalized['location_norm'].unique()}")
    print(f"   - Date: {input_date} between start_date and end_date")
    
    # Filter step by step for debugging
    material_matches = df_normalized[df_normalized['material_norm'] == material_clean]
    print(f"🔍 Material matches: {len(material_matches)}")
    
    unit_matches = material_matches[material_matches['unit_norm'] == unit_clean]
    print(f"🔍 Unit matches: {len(unit_matches)}")
    
    location_matches = unit_matches[unit_matches['location_norm'] == location_clean]
    print(f"🔍 Location matches: {len(location_matches)}")
    
    date_matches = location_matches[
        (location_matches['start_date'] <= input_date) & 
        (location_matches['end_date'] >= input_date)
    ]
    print(f"🔍 Date matches: {len(date_matches)}")
    
    if len(date_matches) == 0:
        # Enhanced error message with debugging info
        error_msg = f"No matching emission factor found for:\n"
        error_msg += f"Material: '{input_data.material}' (normalized: '{material_clean}')\n"
        error_msg += f"Unit: '{input_data.unit}' (normalized: '{unit_clean}')\n"
        error_msg += f"Location: '{input_data.location}' (normalized: '{location_clean}')\n"
        error_msg += f"Date: {input_data.date_of_activity} ({input_date})\n"
        
        # Show available options
        if len(material_matches) > 0:
            error_msg += f"Available units for this material: {material_matches['unit_norm'].unique()}\n"
        if len(unit_matches) > 0:
            error_msg += f"Available locations for this material/unit: {unit_matches['location_norm'].unique()}\n"
        if len(location_matches) > 0:
            error_msg += f"Available date ranges for this combination:\n"
            for _, row in location_matches.iterrows():
                error_msg += f"  - {row['start_date'].date()} to {row['end_date'].date()}\n"
        
        raise ValueError(error_msg)
    
    # Use the first match (you might want to add logic to handle multiple matches)
    factor = date_matches.iloc[0]
    emission = input_data.quantity * factor['value']
    
    print(f"✅ Match found! Factor: {factor['value']}, Emission: {emission}")
    
    return EmissionOutput(
        emission_kg_co2e=round(emission, 3),
        emission_factor_used=factor['value'],
        factor_unit=factor['unit'],
        factor_source=factor['source'],
        valid_from=factor['start_date'].date(),
        valid_to=factor['end_date'].date()
    )

def save_emission_record(record: EmissionRecord, file_path="processed/emission_records.csv"):
    # Convert to dict
    record_dict = record.model_dump()  # Use model_dump() instead of dict() for newer Pydantic versions
    
    # Append or create new file
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df = pd.concat([df, pd.DataFrame([record_dict])], ignore_index=True)
    else:
        df = pd.DataFrame([record_dict])
    
    df.to_csv(file_path, index=False)
    print(f"💾 Saved emission record to {file_path}")

def get_yoy_emissions(file_path="processed/emission_records.csv") -> dict:
    if not os.path.exists(file_path):
        raise ValueError("No emission records found yet.")
    
    df = pd.read_csv(file_path, parse_dates=["date_of_activity"])
    df["year"] = df["date_of_activity"].dt.year
    
    grouped = df.groupby("year")["emission_kg_co2e"].sum().to_dict()
    
    current_year = max(grouped.keys(), default=None)
    previous_year = current_year - 1 if current_year else None
    
    result = {
        "current_year": {
            "scope1": round(grouped.get(current_year, 0), 2),
            "scope2": 0
        },
        "previous_year": {
            "scope1": round(grouped.get(previous_year, 0), 2),
            "scope2": 0
        }
    }
    
    prev = result["previous_year"]["scope1"]
    curr = result["current_year"]["scope1"]
    
    if prev > 0:
        result["change_percentage"] = round(((curr - prev) / prev) * 100, 2)
    else:
        result["change_percentage"] = 100.0 if curr > 0 else 0.0
    
    return result

def get_emission_intensity(
    records_path="processed/emission_records.csv",
    metrics_path="processed/business_metrics.csv",
    metric_name="Tons of Steel Produced"
) -> dict:
    print(f"🔍 Checking emission intensity...")
    print(f"📂 Records path: {records_path} (exists: {os.path.exists(records_path)})")
    print(f"📂 Metrics path: {metrics_path} (exists: {os.path.exists(metrics_path)})")
    
    # Check if files exist
    if not os.path.exists(records_path):
        raise ValueError(f"Emission records file not found: {records_path}")
    if not os.path.exists(metrics_path):
        raise ValueError(f"Business metrics file not found: {metrics_path}")
    
    # Read data
    df_emissions = pd.read_csv(records_path, parse_dates=["date_of_activity"])
    df_metrics = pd.read_csv(metrics_path, parse_dates=["date"])
    
    print(f"📊 Loaded {len(df_emissions)} emission records")
    print(f"📊 Loaded {len(df_metrics)} business metrics")
    
    # Filter metrics for the specified metric name
    df_metrics_filtered = df_metrics[df_metrics["metric_name"] == metric_name]
    print(f"📊 Filtered to {len(df_metrics_filtered)} metrics for '{metric_name}'")
    
    if len(df_emissions) == 0:
        return {"message": "No emission records found"}
    
    if len(df_metrics_filtered) == 0:
        available_metrics = df_metrics["metric_name"].unique().tolist()
        return {
            "error": f"No metrics found for '{metric_name}'",
            "available_metrics": available_metrics
        }
    
    # Group emissions monthly using year-month format
    df_emissions["year_month"] = df_emissions["date_of_activity"].dt.to_period("M")
    monthly_emissions = df_emissions.groupby("year_month")["emission_kg_co2e"].sum()
    
    # Group metrics monthly using year-month format  
    df_metrics_filtered["year_month"] = df_metrics_filtered["date"].dt.to_period("M")
    monthly_metrics = df_metrics_filtered.groupby("year_month")["value"].sum()
    
    print(f"📊 Monthly emissions periods: {len(monthly_emissions)}")
    print(f"📊 Monthly metrics periods: {len(monthly_metrics)}")
    
    # Convert to DataFrame for easier handling
    df_emissions_monthly = monthly_emissions.reset_index()
    df_metrics_monthly = monthly_metrics.reset_index()
    
    # Merge on year_month
    df_combined = pd.merge(
        df_emissions_monthly, 
        df_metrics_monthly, 
        on="year_month", 
        how="inner"
    )
    
    print(f"📊 Combined periods: {len(df_combined)}")
    
    if len(df_combined) == 0:
        return {
            "message": "No overlapping periods found between emissions and metrics",
            "emission_periods": [str(p) for p in monthly_emissions.index],
            "metric_periods": [str(p) for p in monthly_metrics.index]
        }
    
    # Calculate intensity
    df_combined["intensity"] = df_combined["emission_kg_co2e"] / df_combined["value"]
    
    # Create result dictionary
    result = {}
    for _, row in df_combined.iterrows():
        period_str = str(row["year_month"])
        result[period_str] = round(row["intensity"], 4)
    
    print(f"✅ Successfully calculated intensity for {len(result)} periods")
    return result

def get_emission_hotspot(file_path="processed/emission_records.csv") -> dict:
    if not os.path.exists(file_path):
        raise ValueError("No emission records found.")
    
    df = pd.read_csv(file_path)
    
    if "material" not in df.columns or "emission_kg_co2e" not in df.columns:
        raise ValueError("Missing required columns.")
    
    result = df.groupby("material")["emission_kg_co2e"].sum().sort_values(ascending=False)
    return result.round(2).to_dict()