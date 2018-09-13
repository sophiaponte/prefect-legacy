import datetime
import uuid
from contextlib import contextmanager
from typing import Any, Callable, Dict, Iterable

import prefect
from prefect.utilities.json import Serializable


class Executor(Serializable):
    """
    Base Executor class which all other executors inherit from.
    """

    def __init__(self):
        self.executor_id = type(self).__name__ + ": " + str(uuid.uuid4())

    @contextmanager
    def start(self) -> Iterable[None]:
        """
        Context manager for initializing execution.

        Any initialization this executor needs to perform should be done in this
        context manager, and torn down after yielding.
        """
        yield

    def map(
        self, fn: Callable, *args: Any, maps=None, upstream_states=None, **kwargs: Any
    ) -> Any:
        """
        Submit a function to be mapped over.

        Args:
            - fn (Callable): function which is being submitted for execution
            - *args (Any): arguments to be passed to `fn` with each call
            - maps (dict): dictionary of keyword name -> [State] which represent
                the arguments to map `fn` over.  The special key `None` is reserved for
                a list of upstream dependencies which do not have any associated `key`
            - upstream_states ([State]): a list of upstream dependencies which
                are not keyword arguments to be passed on each call
            - **kwargs (Any): keyword arguments to be passed to `fn` with each
                call

        Returns:
            - [Futures]: an iterable of future-like objects
        """
        raise NotImplementedError()

    def submit(self, fn: Callable, *args: Any, **kwargs: Any) -> Any:
        """
        Submit a function to the executor for execution. Returns a future.

        Args:
            - fn (Callable): function which is being submitted for execution
            - *args (Any): arguments to be passed to `fn`
            - **kwargs (Any): keyword arguments to be passed to `fn`

        Returns:
            - Any: a future-like object
        """
        raise NotImplementedError()

    def wait(self, futures: Iterable, timeout: datetime.timedelta = None) -> Iterable:
        """
        Resolves futures to their values. Blocks until the future is complete.

        Args:
            - futures (Iterable): iterable of futures to compute
            - timeout (datetime.timedelta): maximum length of time to allow for
                execution

        Returns:
            - Iterable: an iterable of resolved futures
        """
        raise NotImplementedError()

    def queue(self, maxsize=0):
        """
        Creates an executor-compatible Queue object which can share state
        across tasks.

        Args:
            - maxsize (int): maxsize of the queue; defaults to 0 (infinite)

        Returns:
            - Queue: an executor compatible queue which can be shared among
                tasks
        """
        raise NotImplementedError()

    def submit_with_context(
        self, fn: Callable, *args: Any, context: Dict, **kwargs: Any
    ) -> Any:
        """
        Submit a function to the executor that will be run in a specific Prefect context.

        Args:
            - fn (Callable): function which is being submitted for execution
            - *args (Any): arguments to be passed to `fn`
            - context (dict): `prefect.utilities.Context` to be used in function execution
            - **kwargs (Any): keyword arguments to be passed to `fn`

        Returns:
            - Any: a future-like object
        """

        def run_fn_in_context(*args, context, **kwargs):
            with prefect.context(context):
                return fn(*args, **kwargs)

        return self.submit(run_fn_in_context, *args, context=context, **kwargs)
