import json
import os
from datetime import datetime, timezone
from pathlib import Path

LOG_FILE = Path("sessions/session_log.jsonl")

def log_exchange(prompt: str, response: str, model: str = "claude-sonnet-4-20250514", metadata: dict = None):
    """
    Capture un échange prompt/réponse avec timestamp UTC.
    Écrit une ligne JSON dans le fichier de log.
    """
    LOG_FILE.parent.mkdir(exist_ok=True)
    
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "model": model,
        "prompt": prompt,
        "response": response,
        "metadata": metadata or {}
    }
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    
    return entry