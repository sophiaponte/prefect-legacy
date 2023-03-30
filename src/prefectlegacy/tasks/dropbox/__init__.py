"""
Tasks that interface with Dropbox.
"""
try:
    from prefectlegacy.tasks.dropbox.dropbox import DropboxDownload
except ImportError as err:
    raise ImportError(
        'Using `prefectlegacy.tasks.dropbox` requires Prefect to be installed with the "dropbox" extra.'
    ) from err

__all__ = ["DropboxDownload"]
