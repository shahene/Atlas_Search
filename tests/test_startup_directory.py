from startup_directory import search

def test_search_finds_document_by_tag():
    results = search("payments")
    titles = [document["title"] for document in results]
    assert "Stripe" in titles

def test_search_returns_empty_list_when_nothing_matches():
    assert search("quantum") == []