import json
import os
from datetime import datetime
import hashlib

LOG_FILE = "logs/tasks.json"

def log_task(input_text, output):
    os.makedirs("logs", exist_ok=True)

    timestamp = datetime.utcnow().isoformat()

    record = {
        "input": input_text,
        "output": output,
        "timestamp": timestamp
    }

    # hash (blockchain-like)
    record_str = json.dumps(record, sort_keys=True)
    record["hash"] = hashlib.sha256(record_str.encode()).hexdigest()

    try:
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(record)

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=2)

    return record