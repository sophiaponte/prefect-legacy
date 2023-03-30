"""
This module contains a collection of tasks for interacting with Azure Machine Learning Service resources.
"""

try:
    from prefectlegacy.tasks.azureml.dataset import (
        DatasetCreateFromDelimitedFiles,
        DatasetCreateFromParquetFiles,
        DatasetCreateFromFiles,
    )

    from prefectlegacy.tasks.azureml.datastore import (
        DatastoreRegisterBlobContainer,
        DatastoreList,
        DatastoreGet,
        DatastoreUpload,
    )

except ImportError as err:
    raise ImportError(
        'Using `prefectlegacy.tasks.azureml` requires Prefect to be installed with the "azureml" extra.'
    ) from err

__all__ = [
    "DatasetCreateFromDelimitedFiles",
    "DatasetCreateFromFiles",
    "DatasetCreateFromParquetFiles",
    "DatastoreGet",
    "DatastoreList",
    "DatastoreRegisterBlobContainer",
    "DatastoreUpload",
]
