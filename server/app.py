from fastapi import FastAPI
from server.environment import FraudEnv
from tasks.easy import transactions as easy_transactions

app = FastAPI()

# Global environment (IMPORTANT)
GLOBAL_ENV = None

# -------------------------------
# 🔁 RESET ENDPOINT
# -------------------------------
@app.post("/reset")
def reset():
    global GLOBAL_ENV

    # Initialize environment
    GLOBAL_ENV = FraudEnv(easy_transactions)
    result = GLOBAL_ENV.reset()

    return {
        "state": result["state"],
        "reward": result["reward"],
        "done": result["done"]
    }

# -------------------------------
# 🔁 STEP ENDPOINT
# -------------------------------
@app.post("/step")
def step(action: dict):
    global GLOBAL_ENV

    result = GLOBAL_ENV.step(action["action"])

    return {
        "state": result["state"],
        "reward": result["reward"],
        "done": result["done"]
    }

# -------------------------------
# ❤️ HEALTH CHECK
# -------------------------------
@app.get("/health")
def health():
    return {"status": "ok"}