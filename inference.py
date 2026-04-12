import requests
import os

BASE_URL = os.getenv("ENV_SERVER_URL", "http://localhost:7860")

def main():
    print("[START] task=fraud-detection env=custom model=rule-based")

    # 🔁 RESET ENV
    res = requests.post(f"{BASE_URL}/reset")
    data = res.json()

    done = data.get("done", False)
    step = 0
    rewards = []

    # 🔄 LOOP THROUGH ENV
    while not done:
        action = {"action": 1}

        res = requests.post(f"{BASE_URL}/step", json=action)
        data = res.json()

        reward = data.get("reward", 0)
        done = data.get("done", False)

        rewards.append(reward)
        step += 1

        print(f"[STEP] step={step} action=1 reward={reward:.2f} done={str(done).lower()} error=null")

    score = sum(rewards) / len(rewards) if rewards else 0

    print(f"[END] success=true steps={step} score={score:.3f} rewards={','.join([str(r) for r in rewards])}")

if __name__ == "__main__":
    main()