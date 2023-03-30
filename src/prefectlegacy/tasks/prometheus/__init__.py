"""
Tasks for interacting with Prometheus. The main task are using pushgateway 
"""
try:
    from prefectlegacy.tasks.prometheus.pushgateway import (
        PushGaugeToGateway,
        PushAddGaugeToGateway,
    )
except ImportError as err:
    raise ImportError(
        'Using `prefectlegacy.tasks.prometheus` requires Prefect to be installed with the "prometheus" extra.'
    ) from err

__all__ = ["PushAddGaugeToGateway", "PushGaugeToGateway"]
