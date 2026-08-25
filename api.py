from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel  # <-- NEW: Import BaseModel
import random  # <-- NEW: Import random for battles
from ledger import house_armies, westeros_map

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- NEW: Define what a march command looks like ---
class MarchCommand(BaseModel):
    attacker: str
    defender: str


# --- NEW: The POST endpoint to execute battles ---
@app.post("/march")
def execute_march(command: MarchCommand):
    attacker = command.attacker
    defender = command.defender

    # 1. Guard clauses (Validation)
    if attacker not in house_armies or defender not in house_armies:
        return {"status": "error", "message": "Invalid house."}

    if defender not in westeros_map.get(attacker, []):
        return {"status": "error", "message": f"{defender} does not border {attacker}."}

    # 2. Battle Logic
    attacker_score = house_armies[attacker] + random.randint(1, 100)
    defender_score = house_armies[defender] + random.randint(1, 100)

    if attacker_score > defender_score:
        result_msg = f"House {attacker} wins the battle with a score of {attacker_score} to {defender_score}!"
    else:
        result_msg = f"House {defender} holds the line with a score of {defender_score} to {attacker_score}!"

    # 3. Return the result back to React
    return {"status": "success", "message": result_msg, "armies": house_armies}


# (Your existing GET routes)
@app.get("/armies")
def get_armies():
    return {"status": "success", "data": house_armies}


@app.get("/map")
def get_map():
    return {"status": "success", "data": westeros_map}
