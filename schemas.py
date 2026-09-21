from pydantic import BaseModel

class StartupSearchResult(BaseModel):
    id: int
    title: str
    body: str
    tags: list[str]

class SearchResponse(BaseModel):
    query: str
    count: int
    results: list[StartupSearchResult]