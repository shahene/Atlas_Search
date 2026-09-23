from fastapi import FastAPI
from database_search import search_companies
from schemas import SearchResponse

app = FastAPI()

@app.get('/search', response_model=SearchResponse)
async def search_startups(query: str) -> SearchResponse:
    results = search_companies(query)
    return SearchResponse(
        query=query,
        count=len(results),
        results=results,
    )
        