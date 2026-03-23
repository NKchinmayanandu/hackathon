import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.feature_extraction.text import CountVectorizer

# -------------------------------
# LOAD DATA (replace this)
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
# PIPELINE
# -------------------------------
pipeline = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("model", LogisticRegression())
])

# -------------------------------
# TRAIN TEST SPLIT
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# TRAIN
# -------------------------------
pipeline.fit(X_train, y_train)

# -------------------------------
# EVA