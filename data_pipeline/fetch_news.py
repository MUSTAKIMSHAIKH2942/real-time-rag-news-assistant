
from utils.factory import NewsFetcherFactory

def fetch_news():
    fetcher = NewsFetcherFactory.get_fetcher('rss')
    return fetcher.fetch()
