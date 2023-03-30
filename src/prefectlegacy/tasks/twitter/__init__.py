"""
Tasks for interacting with Twitter.
"""
try:
    from prefectlegacy.tasks.twitter.twitter import LoadTweetReplies
except ImportError as exc:
    raise ImportError(
        'Using `prefectlegacy.tasks.twitter` requires Prefect to be installed with the "twitter" extra.'
    ) from exc

__all__ = ["LoadTweetReplies"]
