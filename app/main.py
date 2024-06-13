from fastapi import FastAPI
from .api import configuration
from .database import engine
from .models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(configuration.router, prefix="/api")