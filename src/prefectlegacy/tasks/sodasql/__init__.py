"""
This module contains a collection of tasks to run Data Quality tests using soda-sql library
"""

try:
    from prefectlegacy.tasks.sodasql.sodasql_tasks import SodaSQLScan
except ImportError as err:
    raise ImportError(
        'Using `prefectlegacy.tasks.sodasql` requires Prefect to be installed with the "sodasql" extra.'
    ) from err

__all__ = ["SodaSQLScan"]
