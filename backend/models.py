from pydantic import BaseModel
from datetime import date

class EmissionInput(BaseModel):
    material: str
    quantity: float
    unit: str
    date_of_activity: date
    location: str

class EmissionOutput(BaseModel):
    emission_kg_co2e: float
    emission_factor_used: float
    factor_unit: str
    factor_source: str
    valid_from: date
    valid_to: date

class EmissionRecord(BaseModel):
    material: str
    quantity: float
    unit: str
    date_of_activity: date
    location: str
    emission_kg_co2e: float

class BusinessMetric(BaseModel):
    date: date
    metric_name: str
    value: float
