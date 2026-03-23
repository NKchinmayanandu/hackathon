def predict_rule(data: dict):
    query = data.get("query", "")

    q = query.lower()

    q = query.lower()

# Greeting
    if any(word in q for word in ["hello", "hi", "hey"]):
        return {
        "mode": "rule",
        "result": "Greeting detected → automated response sent"
    }

# Exit
    elif any(word in q for word in ["bye", "thanks", "thank you"]):
        return {
        "mode": "rule",
        "result": "Session completed → response delivered"
    }

# Help
    elif "help" in q:
        return {
        "mode": "rule",
        "result": "User requested assistance → guidance provided"
    }
