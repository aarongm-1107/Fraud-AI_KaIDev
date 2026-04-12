from fastapi import FastAPI
from env import FraudEnv
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

    # Load default dataset (easy)
    GLOBAL_ENV = FraudEnv(easy_transactions)
    state = GLOBAL_ENV.reset()

    return {
        "state": state,
        "reward": 0,
        "done": False
    }

# -------------------------------
# 🔁 STEP ENDPOINT
# -------------------------------
@app.post("/step")
def step(action: dict):
    global GLOBAL_ENV

    result = GLOBAL_ENV.step(action["action"])

    return {
        "state": result.next_state,
        "reward": result.reward,
        "done": result.done
    }

# -------------------------------
# ❤️ HEALTH CHECK
# -------------------------------
@app.get("/health")
def health():
    return {"status": "ok"}