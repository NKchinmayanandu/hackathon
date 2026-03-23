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

    pred = model.predict([query])[0]

    try:
        prob = model.predict_proba([query]).max()
    except:
        prob = None

    return {
        "mode": "ml",
        "result": str(pred),
        "confidence": float(prob) if prob else None
    }