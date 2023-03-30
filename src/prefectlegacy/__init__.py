import prefectlegacy.utilities
from prefectlegacy.configuration import config

from prefectlegacy.utilities.context import context
from prefectlegacy.utilities.plugins import API as api, PLUGINS as plugins, MODELS as models

from prefectlegacy.client import Client
import prefectlegacy.schedules
import prefectlegacy.triggers
import prefectlegacy.storage
import prefectlegacy.executors

from prefectlegacy.core import Task, Flow, Parameter
import prefectlegacy.engine
import prefectlegacy.tasks
from prefectlegacy.tasks.control_flow import case
from prefectlegacy.tasks.core.resource_manager import resource_manager

from prefectlegacy.utilities.tasks import task, tags, apply_map
from prefectlegacy.utilities.edges import mapped, unmapped, flatten

import prefectlegacy.serialization
import prefectlegacy.agent
import prefectlegacy.backend
import prefectlegacy.artifacts

from ._version import get_versions as _get_versions

__version__ = _get_versions()["version"]  # type: ignore
del _get_versions

try:
    import signal as _signal
    from ._siginfo import sig_handler as _sig_handler

    _signal.signal(29, _sig_handler)
except:
    pass

__all__ = [
    "Client",
    "Flow",
    "Parameter",
    "Task",
    "api",
    "apply_map",
    "case",
    "config",
    "context",
    "flatten",
    "mapped",
    "models",
    "plugins",
    "resource_manager",
    "tags",
    "task",
    "unmapped",
]
