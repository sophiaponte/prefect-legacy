"""
Collection of tasks for sending notifications.

Useful for situations in which state handlers are inappropriate.
"""
from prefectlegacy.tasks.notifications.email_task import EmailTask
from prefectlegacy.tasks.notifications.slack_task import SlackTask
from prefectlegacy.tasks.notifications.pushbullet_task import PushbulletTask

__all__ = ["EmailTask", "PushbulletTask", "SlackTask"]
