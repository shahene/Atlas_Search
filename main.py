from fastapi import FastAPI
from startup_directory import search
from schemas import SearchResponse

app = FastAPI()

@app.get('/search', response_model=SearchResponse)
async def search_startups(query: str) -> SearchResponse:
    results = search(query)
    return SearchResponse(
        query=query,
        count=len(results),
        results=results,
    )
        