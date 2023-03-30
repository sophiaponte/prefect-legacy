"""
The Result classes in this `prefectlegacy.engine.result` package are results used internally by the Prefect pipeline to track and store results without persistence.

If you are looking for the API docs for the result subclasses you can use to enable task return value checkpointing or to store task data, see the API docs for the [Result Subclasses in `prefectlegacy.engine.results`](results.html).
"""
import prefectlegacy
from prefectlegacy.engine.result.base import Result, NoResult, NoResultType

__all__ = ["NoResult", "NoResultType", "Result"]
