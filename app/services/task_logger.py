import json
import os
import hashlib
from datetime import datetime

LOG_FILE = "logs/tasks.json"
def log_task(input_text, output):
    os.makedirs("logs", exist_ok=True)

    timestamp = datetime.utcnow().isoformat()

    try:
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    # ✅ THIS LINE MUST EXIST
    prev_hash = data[-1]["hash"] if data else "0"

    record = {
        "block_id": len(data) + 1,
        "input": input_text,
        "output": output,
        "timestamp": timestamp,
        "prev_hash": prev_hash
    }

    record_str = json.dumps(record, sort_keys=True)
    record["hash"] = hashlib.sha256(record_str.encode()).hexdigest()

    data.append(record)

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=2)

    return record