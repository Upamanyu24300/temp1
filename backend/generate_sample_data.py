import pandas as pd
import os
from datetime import datetime, date

# Create test emission factors CSV if it doesn't exist
def create_test_emission_factors():
    """Create a sample emission factors file for testing"""
    
    # Sample data that matches your test input
    sample_data = [
        # 2023 data
        {
            "material": "Petroleum Coke",
            "unit": "tCO2/KL",
            "value": 2.5,
            "source": "EPA Guidelines 2023",
            "location": "Central Steel Plant",
            "start_date": "2023-01-01",
            "end_date": "2023-12-31"
        },
        {
            "material": "Natural Gas",
            "unit": "tCO2/m3",
            "value": 0.002,
            "source": "IPCC 2023",
            "location": "Central Steel Plant",
            "start_date": "2023-01-01",
            "end_date": "2023-12-31"
        },
        {
            "material": "Diesel",
            "unit": "kgCO2/L",
            "value": 2.68,
            "source": "Local Authority 2023",
            "location": "Central Steel Plant",
            "start_date": "2023-01-01",
            "end_date": "2023-12-31"
        },
        
        # 2024 data (with updated factors)
        {
            "material": "Petroleum Coke",
            "unit": "tCO2/KL",
            "value": 2.6,  # Updated factor
            "source": "EPA Guidelines 2024",
            "location": "Central Steel Plant",
            "start_date": "2024-01-01",
            "end_date": "2024-12-31"
        },
        {
            "material": "Natural Gas",
            "unit": "tCO2/m3",
            "value": 0.0022,  # Updated factor
            "source": "IPCC 2024",
            "location": "Central Steel Plant",
            "start_date": "2024-01-01",
            "end_date": "2024-12-31"
        },
        {
            "material": "Diesel",
            "unit": "kgCO2/L",
            "value": 2.70,  # Updated factor
            "source": "Local Authority 2024",
            "location": "Central Steel Plant",
            "start_date": "2024-01-01",
            "end_date": "2024-12-31"
        },
        
        # Additional locations for testing
        {
            "material": "Petroleum Coke",
            "unit": "tCO2/KL",
            "value": 2.4,
            "source": "Regional Standards 2023",
            "location": "North Steel Plant",
            "start_date": "2023-01-01",
            "end_date": "2023-12-31"
        },
        {
            "material": "Petroleum Coke",
            "unit": "tCO2/KL",
            "value": 2.45,
            "source": "Regional Standards 2024",
            "location": "North Steel Plant",
            "start_date": "2024-01-01",
            "end_date": "2024-12-31"
        }
    ]
    
    # Create DataFrame
    df = pd.DataFrame(sample_data)
    
    # Convert date columns to datetime
    df["start_date"] = pd.to_datetime(df["start_date"])
    df["end_date"] = pd.to_datetime(df["end_date"])
    
    # Ensure processed directory exists
    os.makedirs("processed", exist_ok=True)
    
    # Save to CSV
    output_path = "processed/emission_factors.csv"
    df.to_csv(output_path, index=False)
    
    print(f"✅ Created test emission factors file: {output_path}")
    print(f"📊 Records created: {len(df)}")
    print(f"🗓️ Date range: {df['start_date'].min()} to {df['end_date'].max()}")
    
    return df

def create_sample_business_metrics():
    """Create sample business metrics for testing"""
    
    # Generate monthly data for 2023 and 2024
    dates_2023 = pd.date_range(start="2023-01-01", end="2023-12-31", freq="M")
    dates_2024 = pd.date_range(start="2024-01-01", end="2024-12-31", freq="M")
    
    business_metrics = []
    
    for date_val in list(dates_2023) + list(dates_2024):
        business_metrics.extend([
            {
                "date": date_val.strftime("%Y-%m-%d"),
                "metric_name": "Tons of Steel Produced",
                "value": 45000 + (date_val.month * 2000)  # Seasonal variation
            },
            {
                "date": date_val.strftime("%Y-%m-%d"),
                "metric_name": "Number of Employees",
                "value": 950 + (date_val.month * 5)
            }
        ])
    
    df_metrics = pd.DataFrame(business_metrics)
    
    # Ensure processed directory exists
    os.makedirs("processed", exist_ok=True)
    
    # Save to CSV
    output_path = "processed/business_metrics.csv"
    df_metrics.to_csv(output_path, index=False)
    
    print(f"✅ Created sample business metrics: {output_path}")
    print(f"📊 Records created: {len(df_metrics)}")
    
    return df_metrics

def test_emission_calculation():
    """Test the emission calculation with your sample data"""
    
    # Import your models and logic
    from models import EmissionInput
    from emissions_logic import calculate_emissions
    
    # Test data that should work
    test_input = EmissionInput(
        material="Petroleum Coke",
        quantity=350,
        unit="tCO2/KL",
        date_of_activity=date(2023, 6, 23),
        location="Central Steel Plant"
    )
    
    try:
        result = calculate_emissions(test_input)
        print(f"✅ Test successful!")
        print(f"🧮 Input: {test_input}")
        print(f"📊 Result: {result}")
        return True
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Creating test data for Carbon Emissions Platform...")
    print("=" * 50)
    
    # Create test data
    df_factors = create_test_emission_factors()
    df_metrics = create_sample_business_metrics()
    
    print("\n" + "=" * 50)
    print("🧪 Testing emission calculation...")
    
    # Test the calculation
    success = test_emission_calculation()
    
    if success:
        print("\n🎉 All tests passed! Your system is ready to use.")
    else:
        print("\n⚠️  Tests failed. Please check the error messages above.")
    
    print("\n📋 Sample API request that should work:")
    print("""
    {
        "material": "Petroleum Coke",
        "quantity": 350,
        "unit": "tCO2/KL",
        "date_of_activity": "2023-06-23",
        "location": "Central Steel Plant"
    }
    """)