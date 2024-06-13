from sqlalchemy.orm import Session
from . import models, schemas

def create_configuration(db: Session, configuration: schemas.ConfigurationCreate):
    db_configuration = models.Configuration(**configuration.dict())
    db.add(db_configuration)
    db.commit()
    db.refresh(db_configuration)
    return db_configuration

def get_configuration(db: Session, country_code: str):
    return db.query(models.Configuration).filter(models.Configuration.country_code == country_code).first()

def update_configuration(db: Session, country_code: str, configuration: schemas.ConfigurationUpdate):
    db_configuration = db.query(models.Configuration).filter(models.Configuration.country_code == country_code).first()
    if db_configuration:
        db_configuration.business_name = configuration.business_name
        db_configuration.registration_number = configuration.registration_number
        db_configuration.extra_details = configuration.extra_details
        db.commit()
        db.refresh(db_configuration)
    return db_configuration

def delete_configuration(db: Session, country_code: str):
    db_configuration = db.query(models.Configuration).filter(models.Configuration.country_code == country_code).first()
    if db_configuration:
        db.delete(db_configuration)
        db.commit()
    return db_configuration