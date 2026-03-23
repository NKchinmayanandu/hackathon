import pickle
import pandas as pd

with open("ml/model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_rule(data: dict):
    query = data.get("query", "")

    if "hello" in query.lower():
        return {"mode": "rule", "result": "Hi 👋"}
    elif "bye" in query.lower():
        return {"mode": "rule", "result": "Goodbye 👋"}
    
    return {
        "mode": "rule",
        "result": "Default response"
    }

