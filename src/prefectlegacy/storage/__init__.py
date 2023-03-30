"""
The Prefect Storage interface encapsulates logic for storing flows. Each
storage unit is able to store _multiple_ flows (with the constraint of name
uniqueness within a given unit).
"""

from warnings import warn

import prefectlegacy
from prefectlegacy import config
from prefectlegacy.storage.base import Storage
from prefectlegacy.storage.azure import Azure
from prefectlegacy.storage.bitbucket import Bitbucket
from prefectlegacy.storage.codecommit import CodeCommit
from prefectlegacy.storage.docker import Docker
from prefectlegacy.storage.gcs import GCS
from prefectlegacy.storage.github import GitHub
from prefectlegacy.storage.gitlab import GitLab
from prefectlegacy.storage.local import Local
from prefectlegacy.storage.module import Module
from prefectlegacy.storage.s3 import S3
from prefectlegacy.storage.webhook import Webhook
from prefectlegacy.storage.git import Git


def get_default_storage_class() -> type:
    """
    Returns the `Storage` class specified in
    `prefectlegacy.config.flows.defaults.storage.default_class`. If the value is a string, it will
    attempt to load the already-imported object. Otherwise, the value is returned.

    Defaults to `Local` if the string config value can not be loaded
    """
    config_value = config.flows.defaults.storage.default_class
    if isinstance(config_value, str):
        try:
            return prefectlegacy.utilities.serialization.from_qualified_name(config_value)
        except ValueError:
            warn(
                f"Could not import {config_value}; using prefectlegacy.storage.Local instead."
            )
            return Local
    else:
        return config_value


__all__ = [
    "Azure",
    "Bitbucket",
    "CodeCommit",
    "Docker",
    "GCS",
    "Git",
    "GitHub",
    "GitLab",
    "Local",
    "Module",
    "S3",
    "Storage",
    "Webhook",
]
