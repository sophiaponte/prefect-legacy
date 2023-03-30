from warnings import warn
from prefectlegacy import config
import prefectlegacy.executors
import prefectlegacy.engine.state
import prefectlegacy.engine.signals
import prefectlegacy.engine.result
from prefectlegacy.engine.flow_runner import FlowRunner
from prefectlegacy.engine.task_runner import TaskRunner
import prefectlegacy.engine.cloud


def get_default_executor_class() -> type:
    """
    Returns the `Executor` class specified in
    `prefectlegacy.config.engine.executor.default_class`. If the value is a string, it will
    attempt to load the already-imported object. Otherwise, the value is returned.

    Defaults to `LocalExecutor` if the string config value can not be loaded
    """
    config_value = config.engine.executor.default_class

    if isinstance(config_value, str):
        try:
            return prefectlegacy.utilities.serialization.from_qualified_name(config_value)
        except ValueError:
            warn(
                "Could not import {}; using "
                "prefectlegacy.executors.LocalExecutor instead.".format(config_value)
            )
            return prefectlegacy.executors.LocalExecutor
    else:
        return config_value


def get_default_flow_runner_class() -> type:
    """
    Returns the `FlowRunner` class specified in
    `prefectlegacy.config.engine.flow_runner.default_class` If the value is a string, it will
    attempt to load the already-imported object. Otherwise, the value is returned.

    Defaults to `FlowRunner` if the string config value can not be loaded
    """
    config_value = config.engine.flow_runner.default_class

    if isinstance(config_value, str):
        try:
            return prefectlegacy.utilities.serialization.from_qualified_name(config_value)
        except ValueError:
            warn(
                "Could not import {}; using "
                "prefectlegacy.engine.flow_runner.FlowRunner instead.".format(config_value)
            )
            return prefectlegacy.engine.flow_runner.FlowRunner
    else:
        return config_value


def get_default_task_runner_class() -> type:
    """
    Returns the `TaskRunner` class specified in `prefectlegacy.config.engine.task_runner.default_class` If the
    value is a string, it will attempt to load the already-imported object. Otherwise, the
    value is returned.

    Defaults to `TaskRunner` if the string config value can not be loaded
    """
    config_value = config.engine.task_runner.default_class

    if isinstance(config_value, str):
        try:
            return prefectlegacy.utilities.serialization.from_qualified_name(config_value)
        except ValueError:
            warn(
                "Could not import {}; using "
                "prefectlegacy.engine.task_runner.TaskRunner instead.".format(config_value)
            )
            return prefectlegacy.engine.task_runner.TaskRunner
    else:
        return config_value


__all__ = ["FlowRunner", "TaskRunner"]
