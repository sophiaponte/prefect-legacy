"""
A collection of tasks for interacting with Airtable.
"""
try:
    from prefectlegacy.tasks.airtable.airtable import WriteAirtableRow, ReadAirtableRow
except ImportError as err:
    raise ImportError(
        'Using `prefectlegacy.tasks.airtable` requires Prefect to be installed with the "airtable" extra.'
    ) from err

__all__ = ["ReadAirtableRow", "WriteAirtableRow"]
