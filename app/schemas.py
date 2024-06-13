from pydantic import BaseModel, Field
from typing import Dict, Any

class ConfigurationBase(BaseModel):
    country_code: str
    business_name:str
    registration_number:str
    extra_details: Dict[str, Any]

class ConfigurationCreate(ConfigurationBase):
    pass

class ConfigurationUpdate(BaseModel):
    country_code: str
    business_name:str
    registration_number:str
    extra_details: Dict[str, Any]

class Configuration(ConfigurationBase):
    business_name: str
    registration_number: str
    extra_details: Dict[str, Any] = Field({}, description="Additional details specific to the country")
    class Config:
        orm_mode = True
    
