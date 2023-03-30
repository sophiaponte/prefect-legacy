"""
Tasks for interacting with SendGrid.
"""
try:
    from prefectlegacy.tasks.sendgrid.sendgrid import SendEmail
except ImportError as exc:
    raise ImportError(
        'Using `prefectlegacy.tasks.sendgrid` requires Prefect to be installed with the "sendgrid" extra.'
    ) from exc

__all__ = ["SendEmail"]
