"""
This module contains a collection of tasks to produce and consume Kafka events
"""

try:
    from prefectlegacy.tasks.kafka.kafka import KafkaBatchConsume, KafkaBatchProduce
except ImportError as err:
    raise ImportError(
        'Using `prefectlegacy.tasks.kafka` requires Prefect to be installed with the "kafka" extra.'
    ) from err

__all__ = ["KafkaBatchConsume", "KafkaBatchProduce"]
