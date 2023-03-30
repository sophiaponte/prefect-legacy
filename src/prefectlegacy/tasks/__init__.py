# only tasks that don't require `extras` should be automatically imported here;
# others must be explicitly imported so they can raise helpful errors if appropriate

from prefectlegacy.core.task import Task
import prefectlegacy.tasks.core
import prefectlegacy.tasks.control_flow
import prefectlegacy.tasks.files
import prefectlegacy.tasks.database
import prefectlegacy.tasks.docker
import prefectlegacy.tasks.github
import prefectlegacy.tasks.notifications
import prefectlegacy.tasks.secrets
import prefectlegacy.tasks.shell

__all__ = ["Task"]
