from sqlalchemy import Column, String, JSON
from .database import Base

class Configuration(Base):
    __tablename__ = "configurations"
    
    country_code = Column(String, primary_key=True, index=True)
    business_name = Column(String)
    registration_number = Column(String)


    extra_details = Column(JSON, nullable=False)