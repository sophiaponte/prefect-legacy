"""
A collection of tasks for interacting with Google Sheets.
"""
try:
    from prefectlegacy.tasks.gsheets.gsheets import (
        WriteGsheetRow,
        ReadGsheetRow,
    )
except ImportError as err:
    raise ImportError(
        'Using `prefectlegacy.tasks.gsheets` requires Prefect to be installed with the "gsheets" extra.'
    ) from err

__all__ = ["ReadGsheetRow", "WriteGsheetRow"]
