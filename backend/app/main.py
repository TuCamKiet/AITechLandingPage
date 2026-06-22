from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.landing_api import router as landing_router

app = FastAPI(
    title="AITeach API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(landing_router)


@app.get("/")
def root():
    return {
        "message": "AITeach API Running"
    }