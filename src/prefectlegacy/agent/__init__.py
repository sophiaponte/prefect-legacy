# only agents that don't require `extras` should be automatically imported here;
# others must be explicitly imported so they can raise helpful errors if appropriate

from prefectlegacy.agent.agent import Agent
import prefectlegacy.agent.docker
import prefectlegacy.agent.kubernetes
import prefectlegacy.agent.local
import prefectlegacy.agent.ecs
import prefectlegacy.agent.vertex

__all__ = ["Agent"]
