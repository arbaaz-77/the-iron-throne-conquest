from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # 1. Import the CORS tool
from ledger import house_armies, westeros_map

app = FastAPI()

# 2. Add the CORS middleware to allow your React app
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],  # Your frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all types of requests (GET, POST, etc.)
    allow_headers=["*"],
)


@app.get("/armies")
def get_armies():
    return {"status": "success", "data": house_armies}


@app.get("/map")
def get_map():
    return {"status": "success", "data": westeros_map}
