from fastapi import FastAPI
from startup_directory import search
app = FastAPI()

@app.get('/search')
async def root(query: str):
    result = search(query)
    return {
        "query": query,
        "results": result
        }