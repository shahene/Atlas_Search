import json
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "startups.json"

def load_documents() -> list[dict]:
    with open(DATA_PATH, "r") as f:
        return json.load(f)


def search(query: str) -> list[str]:
    """Return startup names matching query by exact name or tag substring"""
    result = []
    
    for n in startups:
        if n.lower() == query.lower():
            result.append(n)
            continue
        for param in startups[n]:
            if query.lower() in param.lower():
                result.append(n)
                break
    
    return result

