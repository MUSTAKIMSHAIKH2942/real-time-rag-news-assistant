
from data_pipeline.fetch_news import fetch_news

def test_fetch_news():
    result = fetch_news()
    assert isinstance(result, list)
    assert len(result) > 0
