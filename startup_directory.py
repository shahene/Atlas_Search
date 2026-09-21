import json
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "startups.json"

def load_documents() -> list[dict]:
    with open(DATA_PATH, "r") as f:
        return json.load(f)


def search(query: str) -> list[dict]:
    """Return documents where the query appears in the title, body, or tags"""
    normalized_query = query.lower().strip()
    if not normalized_query:
        return []
    results = []

    for document in load_documents():
        searchable_text = " ".join (
            [
                document["title"],
                document["body"],
                " ".join(document["tags"])
            ]
        ).lower()


        if normalized_query in searchable_text:
            results.append(document)
            print(document)
    
    return results

