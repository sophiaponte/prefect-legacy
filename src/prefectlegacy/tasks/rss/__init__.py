"""
Tasks for interacting with RSS feeds.
"""
try:
    from prefectlegacy.tasks.rss.feed import ParseRSSFeed
except ImportError as err:
    raise ImportError(
        'Using `prefectlegacy.tasks.rss` requires Prefect to be installed with the "rss" extra.'
    ) from err

__all__ = ["ParseRSSFeed"]
