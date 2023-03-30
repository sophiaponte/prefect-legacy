"""
This module contains a collection of tasks for interacting with Exasol databases via
the pyexasol library.
"""
try:
    from prefectlegacy.tasks.exasol.exasol import (
        ExasolFetch,
        ExasolExecute,
        ExasolImportFromIterable,
        ExasolExportToFile,
    )
except ImportError as exc:
    raise ImportError(
        'Using `prefectlegacy.tasks.exasol` requires Prefect to be installed with the "exasol" extra.'
    ) from exc

__all__ = [
    "ExasolExecute",
    "ExasolExportToFile",
    "ExasolFetch",
    "ExasolImportFromIterable",
]
