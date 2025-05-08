
class NewsFetcher:
    def fetch(self):
        raise NotImplementedError

class RSSFetcher(NewsFetcher):
    def fetch(self):
        return ['RSS article 1', 'RSS article 2']

class NewsFetcherFactory:
    @staticmethod
    def get_fetcher(source_type):
        if source_type == 'rss':
            return RSSFetcher()
        raise ValueError('Unknown source type')
