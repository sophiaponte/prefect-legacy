"""
This module contains a collection of tasks for interacting with Firebolt databases via
the firebolt-python-sdk library.
"""

try:
    from prefectlegacy.tasks.firebolt.firebolt import FireboltQuery
except ImportError as err:
    raise ImportError(
        'Using `prefectlegacy.tasks.firebolt` requires Prefect to be installed with the "firebolt" extra.'
    ) from err
