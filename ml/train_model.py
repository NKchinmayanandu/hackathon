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

        # --- SIMPLE / AUTOMATED ---
        "yoo","hello", "hi", "hey", "yo", "good morning", "good evening",
        "bye", "see you", "thanks", "thank you", "ok", "cool",
        "what's up", "sup", "hello there",

        # --- BUSINESS / ML TASKS ---
        "predict sales",
        "predict revenue",
        "forecast next month sales",
        "analyze business data",
        "generate report",
        "monthly sales prediction",
        "next quarter revenue forecast",
        "analyze customer trends",
        "build report for last month",
        "data analysis for growth",
        "predict demand",
        "sales trend analysis",

        # --- REAL HUMAN STYLE (IMPORTANT) ---
        "i need sales prediction",
        "can you analyze my data",
        "give me next month forecast",
        "bro predict revenue",
        "yo analyze business data",
        "please generate report",
        "i want sales forecast",
        "help me with analysis",
        "need prediction for next month",
        "check trends in my data",

        # --- NOISY / SLANG INPUT ---
        "yoo bro need next month sales prediction",
        "plz analyze this data",
        "hey can u predict revenue",
        "bro i need report asap",
        "yo give forecast",
        "need data insights fast",
        "pls do analysis",
        "can u check sales trend",

        # --- EDGE CASES ---
        "random text",
        "just testing",
        "nothing important",
        "tell me something",
        "i am bored",

        # --- MIXED ---
        "hi can you predict sales",
        "hello i need report",
        "yo analyze this",
        "thanks but also forecast revenue",
    ],

    "target": [
        # simple = 0
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,
        0,0,0,

        # business = 1
        1,1,1,1,1,1,1,1,1,1,1,1,

        # human style = 1
        1,1,1,1,1,1,1,1,1,1,

        # noisy = 1
        1,1,1,1,1,1,1,1,

        # edge = 0
        0,0,0,0,0,

        # mixed = 1
        1,1,1,1
    ]
})

X = df["query"]
y = df["target"]

# -------------------------------
# MODEL
# -------------------------------
pipeline = Pipeline([
    ("vectorizer", CountVectorizer(1,2)),
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