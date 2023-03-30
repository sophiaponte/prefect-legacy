"""
This module contains a collection of tasks for interacting with Azure resources.
"""

try:
    from prefectlegacy.tasks.azure.blobstorage import BlobStorageDownload, BlobStorageUpload
    from prefectlegacy.tasks.azure.cosmosdb import (
        CosmosDBCreateItem,
        CosmosDBReadItems,
        CosmosDBQueryItems,
    )
    from prefectlegacy.tasks.azure.datafactory import (
        DatafactoryCreate,
        PipelineCreate,
        PipelineRun,
    )
except ImportError as err:
    raise ImportError(
        'Using `prefectlegacy.tasks.azure` requires Prefect to be installed with the "azure" extra.'
    ) from err

__all__ = [
    "BlobStorageDownload",
    "BlobStorageUpload",
    "CosmosDBCreateItem",
    "CosmosDBQueryItems",
    "CosmosDBReadItems",
    "DatafactoryCreate",
    "PipelineCreate",
    "PipelineRun",
]
