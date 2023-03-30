"""
Tasks for interacting with any SFTP server.
"""
try:
    from prefectlegacy.tasks.sftp.sftp import SftpDownload, SftpUpload
except ImportError as err:
    raise ImportError(
        'prefectlegacy.tasks.sftp` requires Prefect to be installed with the "sftp" extra.'
    ) from err
