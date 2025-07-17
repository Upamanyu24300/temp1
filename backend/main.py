from fastapi import FastAPI, HTTPException
from emissions_logic import calculate_emissions
from models import EmissionInput, EmissionOutput
from models import EmissionRecord
from emissions_logic import calculate_emissions, save_emission_record
from fastapi.responses import JSONResponse
from emissions_logic import get_yoy_emissions
from emissions_logic import get_emission_intensity
from emissions_logic import get_emission_hotspot
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

app = FastAPI()


# Get frontend URL from environment
frontend_url = os.getenv("FRONTEND_URL", "http://localhost:3000")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        frontend_url,
        "http://localhost:3000",
        "https://frontend-production-a166.up.railway.app"  # Your actual frontend URL
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def root():
    return {"message": "Carbon Emission API is running."}

@app.post("/calculate", response_model=EmissionOutput)
def calculate_emission(input_data: EmissionInput):
    try:
        result = calculate_emissions(input_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/emission-records")
def create_emission_record(input_data: EmissionInput):
    try:
        result = calculate_emissions(input_data)
        record = EmissionRecord(
            material=input_data.material,
            quantity=input_data.quantity,
            unit=input_data.unit,
            date_of_activity=input_data.date_of_activity,
            location=input_data.location,
            emission_kg_co2e=result.emission_kg_co2e
        )
        save_emission_record(record)
        return {"message": "Record saved successfully.", "emission": result}
    except Exception as e:
        import traceback
        traceback.print_exc()  # <-- This will show exact error in backend logs
        raise HTTPException(status_code=500, detail=str(e))

    
@app.get("/analytics/yoy")
def analytics_yoy():
    try:
        return get_yoy_emissions()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/analytics/intensity")
def emission_intensity():
    try:
        return get_emission_intensity()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/analytics/hotspot")
def emission_hotspot():
    try:
        return get_emission_hotspot()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)