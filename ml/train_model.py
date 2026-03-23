import os
print("CURRENT DIR:", os.getcwd())
import pandas as pd
import pickle

from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer

print("🚀 TRAINING STARTED")

# -------------------------------
# DATA
# -------------------------------
df = pd.DataFrame({
    "query": [
        "hello",
        "hi",
        "predict sales",
        "analyze data",
        "bye"
    ],
    "target": [0, 0, 1, 1, 0]
})

X = df["query"]
y = df["target"]

# -------------------------------
# MODEL
# -------------------------------
pipeline = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("model", LogisticRegression())
])

pipeline.fit(X, y)

# -------------------------------
# SAVE
# -------------------------------
os.makedirs("ml", exist_ok=True)

base_dir = os.path.dirname(__file__)
model_path = os.path.join(base_dir, "model.pkl")

with open(model_path, "wb") as f:
    pickle.dump(pipeline, f)

print("Saved at:", model_path)

print("✅ model.pkl CREATED")