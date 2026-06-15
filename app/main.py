from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Cloud Control Plane Risk Analyzer")

app.include_router(router)