from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import router as generate_router
import os

app = FastAPI()

# Allow frontend (Streamlit) to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static video serving
from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")

# Register routes
app.include_router(generate_router)

# Root endpoint
@app.get("/")
def root():
    return {"message": "AutoFanFic API is running."}
