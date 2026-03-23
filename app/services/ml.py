import pickle

model = None

def load_model():
    global model
    if model is None:
        with open("ml/model.pkl", "rb") as f:
            model = pickle.load(f)

def predict_ml(data: dict):
    load_model()

    query = data["query"]

    pred = model.predict([query])[0]   # ✅ THIS WAS MISSING

    label_map = {
        0: "Simple query handled automatically",
        1: "Business-related task → requires processing"
    }

    try:
        prob = model.predict_proba([query]).max()
    except:
        prob = None

    return {
        "mode": "ml",
        "result": label_map.get(pred, "Unknown task"),
        "confidence": float(prob) if prob else None
    }